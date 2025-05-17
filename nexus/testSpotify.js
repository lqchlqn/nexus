// const token = 'BQCUgRqdjn9KKALhv7Debnif1kDbm34AsRHseQhq8C2VY2gpC-xEwHDgkkhHJ1DWHrbzr9Mm9m_kldC1f7UhGVDKzpHuIG9JqAi_-k5Y4xyKOW6rZpFKxzVUw8nKzSqyXV9GRhMkZ1DKz2_VIrD8PLeDbFS_K7s2jjcEaun9eoTTNWt2UC8QzUJFxAmfI5wSCxyGUcty2YSBh0qXuzmZw516iThmxStKrSc5OIEo6FSzTKBuaZPqzUzZYm1Gzli6aow-J3IcBwG26K3dtkRT_oX3Z42SSycE9LeplMPDje_0rg';
// async function fetchWebApi(endpoint, method, body) {
//   const res = await fetch(`https://api.spotify.com/${endpoint}`, {
//     headers: {
//       Authorization: `Bearer ${token}`,
//     },
//     method,
//     body:JSON.stringify(body)
//   });
//   return await res.json();
// }

// async function getTopTracks(){
//   // Endpoint reference : https://developer.spotify.com/documentation/web-api/reference/get-users-top-artists-and-tracks
//   return (await fetchWebApi(
//     'v1/me/top/tracks?time_range=long_term&limit=5', 'GET'
//   )).items;
// }

// const topTracks = await getTopTracks();
// console.log(
//   topTracks?.map(
//     ({name, artists}) =>
//       `${name} by ${artists.map(artist => artist.name).join(', ')}`
//   )
// );



const playlistId = '0rtNY1KiXQghVbeiG4UDm8';

<iframe
  title="Spotify Embed: Recommendation Playlist "
  src={`https://open.spotify.com/embed/playlist/0rtNY1KiXQghVbeiG4UDm8?utm_source=generator&theme=0`}
  width="100%"
  height="100%"
  style={{ minHeight: '360px' }}
  allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"
  loading="lazy"
/>