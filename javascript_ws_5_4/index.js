const searchInput = document.querySelector('.search-box__button')
const searchResult = document.querySelector('.search-result')  

let page = 1 
let limit = 100

// 버튼에 클릭 이벤트 담기
searchInput.addEventListener('click', fetchAlbums)

// axios 요청 전 로더 띄우고 -> 요청 결과를 받아옴
// 그리고 html 만드는 함수를 따로 나눴음.
async function fetchAlbums(page=1, limit=100) {
  const keyword = document.querySelector('.search-box__input').value
  
  // 만약에 들어온 값이 없으면 그냥 return 해머리기
  if (!keyword.trim()) return
  
  // 아니라면 axios 요청
  const API_KEY = 'ee652dc219d87a5ae63a58c1033fa145'
  const BASE_URL = 'http://ws.audioscrobbler.com/2.0/'
  const searchUrl = `?method=album.search&format=json`
  const requestUrl = BASE_URL + searchUrl
  const params = {
    api_key: API_KEY,
    album: keyword,
    page: 1,
    limit: 100,
  }
  
  // 앨범정보 요청
  axios
    .get(requestUrl, { params })
    .then((res) => {
      // 요청 성공
      console.log(res)
      // 앨범들 정보 파싱
      const albums = res.data.results.albummatches.album
      // html문서를 만들 appendAlbumcard 함수로 정보 전달
      appendAlbumCards(albums)
    })
    .catch((err) => {
      // 요청 실패
      alert('잠시 후 다시 시도해주세요.')
    })

}


// 요청 결과를 인자로 받아 html 만들기
function appendAlbumCards(albums) {

  albums.forEach((album) => {
    
    const cardImg = document.createElement('img')
    cardImg.src = album.image[1]['#text']     // sixe = medium 인 image를 고름.

    const cardArtistName = document.createElement('h2')
    cardArtistName.textContent = album.artist

    const cardAlbumName = document.createElement('p')
    cardAlbumName.textContent = album.name

    const cardText = document.createElement('div')
    cardText.classList.add('search-result__text')
    cardText.append(cardArtistName, cardAlbumName)

    const card = document.createElement('div')
    card.classList.add('search-result__card')
    card.append(cardImg, cardText)

    // 앨범 클릭 시 js 로 redirect 하는 코드
    card.addEventListener('click', () => {
      window.location.href = album.url
    })

    searchResult.appendChild(card)
  })

}
