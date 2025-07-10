<div align="center">
  <img src="https://i.imgur.com/Xj1dUCA.jpeg" alt="Amazon Music API" width="700">

# 🎵 Amazon Music API – Unofficial

A **FastAPI REST API** for Amazon Music offering metadata, playback, search, and lookups for tracks, albums, artists, playlists, and podcasts. Includes streaming URL extraction and Widevine DRM key retrieval.
<p>
  <a href="https://github.com/AmineSoukara/amazon-music-api/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/AmineSoukara/amazon-music-api" alt="Contributors">
  </a>
  <a href="https://github.com/AmineSoukara/amazon-music-api/commits/main">
    <img src="https://img.shields.io/github/last-commit/AmineSoukara/amazon-music-api" alt="Last commit">
  </a>
  <a href="https://github.com/AmineSoukara/amazon-music-api/network/members">
    <img src="https://img.shields.io/github/forks/AmineSoukara/amazon-music-api" alt="Forks">
  </a>
  <a href="https://github.com/AmineSoukara/amazon-music-api/stargazers">
    <img src="https://img.shields.io/github/stars/AmineSoukara/amazon-music-api?color=yellow" alt="Stars">
  </a>
  <a href="https://github.com/AmineSoukara/amazon-music-api/issues">
    <img src="https://img.shields.io/github/issues/AmineSoukara/amazon-music-api?color=purple" alt="Open Issues">
  </a>
  <a href="https://github.com/AmineSoukara/amazon-music-api/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/AmineSoukara/amazon-music-api.svg" alt="License">
  </a>
</p>

<h4>
  <a href="https://amazon-music-api.vercel.app">API Docs</a>
  <span> · </span>
  <a href="https://github.com/AmineSoukara/amazon-music-api/issues">Report Bug</a>
  <span> · </span>
  <a href="https://github.com/AmineSoukara/amazon-music-api/issues">Request Feature</a>
</h4>


---
> ⚠️ The API is still in development. For issues or suggestions: [contact support](https://bio.link/aminesoukara). Also This API requires a premium Amazon Music account. If you find it useful and have a premium account you'd like to donate, it would be greatly appreciated. Donations help keep the API running and support multi-region access.

---
## 🔗 Quick Links
- **Base URL**: [Click Here](https://amazon-music-api.vercel.app)

---

## 📚 Endpoints Overview

| Method | Endpoint                            | Description                              |
| ------ | ----------------------------------- | ---------------------------------------- |
| `GET`  | `/login`                          | Get Access Tokens        |
| `GET`  | `/account`                          | Get authenticated account info           |
| `GET`  | `/search?query={query}&type={type}`                           | Search Amazon Music                      |
| `GET`  | `/track?id={track_id}`                 | Get metadata for a track                 |
| `GET`  | `/album?id={album_id}`                 | Get album details including tracks       |
| `GET`  | `/artist?id={artist_id}`               | Get artist info and discography          |
| `GET`  | `/playlist?id={playlist_id}`           | Get official playlist info               |
| `GET`  | `/community_playlist?id={playlist_id}` | Get community playlist info              |
| `GET`  | `/episode?id={episode_id}`             | Get a podcast episode                    |
| `GET`  | `/podcast?id={podcast_id}`             | Get a podcast show and episodes          |
| `GET`  | `/lyrics?id={track_id}`                | Get lyrics            |
| `GET`  | `/stream_urls?id={track_id}`           | Get streaming URLs in multiple qualities |
| `POST` | `/widevine_key`                     | Decrypt Widevine DRM using PSSH          |

---

## ⚠️ Legal Disclaimer

This project is intended for **educational and research purposes only**. It interacts with **Amazon’s internal APIs**, which may **violate their [Terms of Service](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088)**.
The authors are **not affiliated with Amazon**. This software is provided **“as is” without any warranties**, express or implied. Use of this tool is **at your own risk**, and you are solely responsible for ensuring **compliance with applicable laws and terms** in your country or region.
This project is **non-commercial** and does **not host or distribute any Amazon-owned content**.

---

## 👨‍💻 Dev & Support

<a href="https://bio.link/aminesoukara"><img src="https://img.shields.io/badge/@AmineSoukara-000000?style=flat&logo=messenger&logoColor=white&logoWidth=100"></a>
<a href="https://t.me/DezAltySupport"><img src="https://img.shields.io/badge/Group-FF0000?style=flat&logo=telegram&logoColor=white&logoWidth=100"></a>
<a href="https://t.me/DezAlty"><img src="https://img.shields.io/badge/Channel-FF0000?style=flat&logo=telegram&logoColor=white&logoWidth=100"></a>

---

![⭐️](https://telegra.ph/file/b132a131aabe2106bd335.gif)

> ⭐️ If you find this project useful, please consider starring the repo! It helps support the project and keeps it visible to others.


---
</div>
