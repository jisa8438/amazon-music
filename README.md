<div align="center">
  <img src="https://i.imgur.com/1TzoPNy.jpeg" alt="Amazon Music API" width="400">

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
| `GET`  | `/account`                          | Get authenticated account info           |
| `GET`  | `/search`                           | Search Amazon Music                      |
| `GET`  | `/track/{track_id}`                 | Get metadata for a track                 |
| `GET`  | `/album/{album_id}`                 | Get album details including tracks       |
| `GET`  | `/artist/{artist_id}`               | Get artist info and discography          |
| `GET`  | `/playlist/{playlist_id}`           | Get official playlist info               |
| `GET`  | `/community_playlist/{playlist_id}` | Get community playlist info              |
| `GET`  | `/episode/{episode_id}`             | Get a podcast episode                    |
| `GET`  | `/podcast/{podcast_id}`             | Get a podcast show and episodes          |
| `GET`  | `/lyrics/{track_id}`                | Get synced lyrics (LRC format)           |
| `GET`  | `/stream_urls/{track_id}`           | Get streaming URLs in multiple qualities |
| `POST` | `/widevine_key`                     | Decrypt Widevine DRM using PSSH          |

---

## ⚠️ Legal Disclaimer
This project is for educational and research purposes only. It interacts with Amazon's internal APIs, which may violate [Amazon's Terms of Service](https://www.amazon.com/gp/help/customer/display.html?nodeId=508088). The authors are not affiliated with Amazon. Use at your own risk and ensure legal compliance.

---

## 🛡 License

MIT License. See [LICENSE](./LICENSE) for details.

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
