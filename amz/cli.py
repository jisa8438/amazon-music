"""
Amazon-Music
~~~~~~~~~
A Python package for interacting with Amazon Music services.

:Copyright: (c) 2025 By Amine Soukara <https://github.com/AmineSoukara>.
:License: MIT, See LICENSE For More Details.
:Link: https://github.com/AmineSoukara/Amazon-Music
:Description: A comprehensive CLI tool and API wrapper for Amazon Music with download capabilities.
"""

import argparse
import json
import os
import re
import sys
from io import StringIO
from pathlib import Path
from typing import Dict, Optional, Tuple
from urllib.parse import parse_qs, urlparse

import pyfiglet
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from rich.text import Text
from rich.theme import Theme

from .main import AmDownloader

# Regex pattern to parse Amazon Music URLs
REGEX_AMAZON = r"https?://(?:music\.)?(?P<platform>amazon)\.(?:com|[a-z]{2,3})(?:\.[a-z]{2})?/(?:(?P<type>artists|albums|playlists|user-playlists)/)?(?P<id>[A-Za-z0-9]+)(?:\?[^\s]+)?"

# Custom color theme for rich console
custom_theme = Theme(
    {
        "info": "cyan",
        "success": "green",
        "error": "bold red",
        "warning": "yellow",
        "prompt": "magenta",
        "logo": "bold blue",
    }
)

console = Console(theme=custom_theme)

default_path = str(Path.home() / "Music/Amazon Music")
default_path_temp = str(Path(default_path) / "temp")


class AmazonMusicCLI:
    def __init__(self):
        self.parser = self._create_parser()
        self.downloader = None
        self.config_path = Path(__file__).parent / ".amazon_music_config.json"
        self.token = None

    def _create_parser(self) -> argparse.ArgumentParser:
        parser = argparse.ArgumentParser(
            description="Amazon Music Downloader CLI\n\n"
            "Configuration commands:\n"
            "  --config           Interactive configuration setup\n"
            "  --clear-token      Remove stored access token\n"
            "  --show-token       Show the stored access token\n",
            formatter_class=argparse.RawTextHelpFormatter,
            add_help=False,
        )

        parser.add_argument(
            "url_or_id",
            nargs="?",
            help="Amazon Music URL or ID\n"
            "Examples:\n"
            "  - Album: https://music.amazon.com/albums/B08N5KWB9H\n"
            "  - Playlist: https://music.amazon.com/playlists/B08N5KWB9H\n"
            "  - Track ID: B08N5KWB9H",
        )

        parser.add_argument(
            "-q",
            "--quality",
            choices=["Max", "Master", "High", "Normal", "Medium", "Low", "Free"],
            default=None,
            help="Audio quality preference (default: from config)",
        )

        parser.add_argument(
            "-t",
            "--type",
            choices=["auto", "track", "album", "playlist"],
            default="auto",
            help="Content type (default: auto-detect)",
        )

        parser.add_argument(
            "-o",
            "--output",
            default=None,
            help="Output directory (default: from config)",
        )

        parser.add_argument(
            "--temp-dir",
            default=None,
            help="Temporary directory (default: from config)",
        )

        parser.add_argument(
            "--format-folder",
            type=int,
            default=None,
            choices=[1, 2, 3, 4],
            help="Folder naming format (1-4, default: from config)",
        )

        parser.add_argument(
            "--format-track",
            type=int,
            default=None,
            choices=[1, 2, 3, 4],
            help="Track naming format (1-4, default: from config)",
        )

        parser.add_argument(
            "--workers",
            type=int,
            default=None,
            help="Number of parallel download workers (default: from config)",
        )

        parser.add_argument(
            "--zip", action="store_true", help="Create ZIP archive for albums/playlists"
        )

        parser.add_argument(
            "--overwrite", action="store_true", help="Overwrite existing files"
        )

        parser.add_argument(
            "--token",
            help="Amazon Music API access token (will be saved for future use)",
        )

        parser.add_argument(
            "--clear-token", action="store_true", help="Remove stored access token"
        )

        parser.add_argument(
            "--show-token",
            action="store_true",
            help="Show the stored access token (first few characters only)",
        )

        parser.add_argument(
            "--config", action="store_true", help="Interactive configuration setup"
        )

        parser.add_argument(
            "-h", "--help", action="store_true", help="Show this help message and exit"
        )

        return parser

    def print_help(self):
        help_buf = StringIO()
        self.parser.print_help(file=help_buf)
        help_text = help_buf.getvalue()
        console.print(
            Panel.fit(
                help_text, title="[bold cyan]Help[/bold cyan]", border_style="cyan"
            )
        )

    def _load_config(self) -> Dict:
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, "r") as f:
                    return json.load(f)
        except Exception as e:
            console.print(
                f"[warning]Warning: Could not load config - {str(e)}[/warning]"
            )
        return {}

    def _save_config(self, config: Dict):
        try:
            with open(self.config_path, "w") as f:
                json.dump(config, f, indent=4)
            os.chmod(self.config_path, 0o600)
        except Exception as e:
            console.print(
                f"[warning]Warning: Could not save config - {str(e)}[/warning]"
            )

    def _mask_token(self, token: str) -> str:
        """Mask token for display purposes."""
        if not token:
            return "Not set"
        return f"{token[:4]}...{token[-4:]}" if len(token) > 8 else "****"

    def interactive_config(self):
        """Interactive configuration setup."""
        console.print("[bold cyan]Amazon Music Configuration[/bold cyan]")
        console.print("[info]Leave blank to keep current value[/info]")

        config = self._load_config()

        # Token
        current_token = config.get("token", "")
        token = Prompt.ask(
            f"[prompt]Amazon Music API token (current: {
                self._mask_token(current_token)})[/prompt]",
            default="",
            show_default=False,
        )
        if token:
            config["token"] = token

        # Output directory
        current_output = config.get("output", default_path)
        output = Prompt.ask(
            f"[prompt]Default output directory (current: {current_output})[/prompt]",
            default="",
            show_default=False,
        )
        if output:
            config["output"] = output

        # Temp directory
        current_temp = config.get("temp_dir", default_path_temp)
        temp_dir = Prompt.ask(
            f"[prompt]Default temp directory (current: {current_temp})[/prompt]",
            default="",
            show_default=False,
        )
        if temp_dir:
            config["temp_dir"] = temp_dir

        # Quality
        current_quality = config.get("quality", "Normal")
        quality = Prompt.ask(
            f"[prompt]Default quality (current: {current_quality})[/prompt]",
            default="",
            show_default=False,
            choices=["", "Max", "Master", "High", "Normal", "Medium", "Low", "Free"],
        )
        if quality:
            config["quality"] = quality

        # Format folder
        current_folder_fmt = config.get("format_folder", 4)
        folder_fmt = Prompt.ask(
            f"[prompt]Default folder format (1-4) (current: {current_folder_fmt})[/prompt]",
            default="",
            show_default=False,
            choices=["", "1", "2", "3", "4"],
        )
        if folder_fmt:
            config["format_folder"] = int(folder_fmt)

        # Format track
        current_track_fmt = config.get("format_track", 4)
        track_fmt = Prompt.ask(
            f"[prompt]Default track format (1-4) (current: {current_track_fmt})[/prompt]",
            default="",
            show_default=False,
            choices=["", "1", "2", "3", "4"],
        )
        if track_fmt:
            config["format_track"] = int(track_fmt)

        # Workers
        current_workers = config.get("workers", 2)
        workers = Prompt.ask(
            f"[prompt]Default parallel workers (current: {current_workers})[/prompt]",
            default="",
            show_default=False,
        )
        if workers:
            config["workers"] = int(workers)

        self._save_config(config)
        console.print("[success]Configuration saved successfully![/success]")

    def _get_token(self) -> Optional[str]:
        args = self.parser.parse_args()

        if args.clear_token:
            config = self._load_config()

            if config.pop("token", None) is not None:
                self._save_config(config)
                console.print("[info]Stored token has been cleared.[/info]")
            else:
                console.print("[info]No token stored to clear[/info]")

            sys.exit(0)

        if args.show_token:
            config = self._load_config()
            if token := config.get("token"):
                console.print(
                    f"[info]Stored token: {
                        self._mask_token(token)}[/info]"
                )
            else:
                console.print("[info]No token stored[/info]")
            sys.exit(0)

        if args.token:
            config = self._load_config()
            config["token"] = args.token
            self._save_config(config)
            return args.token

        config = self._load_config()
        if "token" in config:
            return config["token"]

        console.print("[error]Error: No access token provided.[/error]")
        console.print("You can:")
        console.print("1. Provide a token with --token argument")
        console.print("2. Enter it now (will be saved for future use)")

        try:
            token = Prompt.ask(
                "[prompt]Enter your Amazon Music API access token[/prompt]"
            ).strip()
            if token:
                config = self._load_config()
                config["token"] = token
                self._save_config(config)
                return token
        except KeyboardInterrupt:
            pass

        console.print("[error]Token is required to use this application.[/error]")
        sys.exit(1)

    def parse_url(self, url: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
        if not (match := re.match(REGEX_AMAZON, url)):
            return None, None, None

        data = match.groupdict()
        query_params = parse_qs(urlparse(url).query)

        # Handle tracks (override type/id if trackAsin exists)
        if track_asin := query_params.get("trackAsin", [None])[0]:
            return data["platform"], "track", track_asin

        # Normalize other types
        type_map = {
            "artists": "artist",
            "albums": "album",
            "playlists": "playlist",
            "user-playlists": "playlist",
        }
        data["type"] = type_map.get(data["type"], data["type"])

        return data["platform"], data["type"], data["id"]

    def run(self):
        args = self.parser.parse_args()

        # Show help and exit if -h/--help present
        if args.help:
            self.print_help()
            sys.exit(0)

        self._print_logo()

        # Handle config command
        if args.config:
            self.interactive_config()
            sys.exit(0)

        # Load config defaults
        config = self._load_config()

        # Get token (handles all token-related operations)
        self.token = self._get_token()
        if not self.token:
            sys.exit(1)

        if not args.url_or_id:
            console.print("[error]Error: No URL or ID provided[/error]")
            self.print_help()
            sys.exit(1)

        # Initialize downloader with config defaults or command line overrides
        self.downloader = AmDownloader(
            path=args.output or config.get("output", default_path),
            path_temp=args.temp_dir or config.get("temp_dir", default_path_temp),
            access_token=self.token,
        )

        _, content_type, content_id = self.parse_url(args.url_or_id)

        if content_type is None and content_id is None:
            content_id = args.url_or_id
            if args.type == "auto":
                console.print(
                    "[error]Could not determine content type from ID. Please specify with --type[/error]"
                )
                sys.exit(1)
            content_type = args.type
        elif args.type != "auto":
            content_type = args.type

        try:
            download_kwargs = {
                "quality": args.quality or config.get("quality", "Normal"),
                "track_format": args.format_track or config.get("format_track", 4),
                "folder_format": args.format_folder or config.get("format_folder", 4),
                "overwrite": args.overwrite,
            }

            if content_type in ["album", "playlist"]:
                download_kwargs.update(
                    {
                        "max_workers": args.workers or config.get("workers", 2),
                        "as_zip": args.zip,
                    }
                )

            if content_type == "track":
                self.download_track(content_id, **download_kwargs)
            elif content_type == "album":
                self.download_album(content_id, **download_kwargs)
            elif content_type == "playlist":
                self.download_playlist(content_id, **download_kwargs)
            else:
                console.print(
                    f"[error]Unsupported content type: {content_type}[/error]"
                )
                sys.exit(1)
        except Exception as e:
            console.print(f"[error]Error during download: {str(e)}[/error]")
            sys.exit(1)

    def download_track(self, track_id: str, **kwargs):
        console.print(f"[info]Downloading track:[/] {track_id}")
        result = self.downloader.download_track(track_id, **kwargs)
        self._handle_result(result)

    def download_album(self, album_id: str, **kwargs):
        console.print(f"[info]Downloading album:[/] {album_id}")
        result = self.downloader.download_album(album_id, **kwargs)
        self._handle_result(result)

    def download_playlist(self, playlist_id: str, **kwargs):
        console.print(f"[info]Downloading playlist:[/] {playlist_id}")
        result = self.downloader.download_playlist(playlist_id, **kwargs)
        self._handle_result(result)

    def _handle_result(self, result):
        if result.success:
            console.print("\n[success]Download successful![/success]")
            if hasattr(result, "tracks") and result.tracks:
                console.print(f"[info]Downloaded {len(result.tracks)} tracks[/info]")
            if hasattr(result, "zip") and result.zip:
                console.print(
                    f"[info]Created ZIP archive: {
                        result.zip}[/info]"
                )
        else:
            console.print("\n[error]Download failed or incomplete[/error]")
            if hasattr(result, "failed") and result.failed:
                console.print(f"[error]Failed tracks: {len(result.failed)}[/error]")
                for track_id in result.failed:
                    console.print(f"- {track_id}")

    def _print_logo(self):
        logo_text = pyfiglet.figlet_format("AMAZON MUSIC", font="doom")
        panel = Panel(
            Text(logo_text, style="logo", justify="center"),
            subtitle="Amazon Music Downloader CLI",
            expand=False,
        )
        console.print(panel)
        console.print()  # Blank line


def main():
    cli = AmazonMusicCLI()
    cli.run()


if __name__ == "__main__":
    main()
