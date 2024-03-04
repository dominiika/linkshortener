export const copyUrlShortened = (urlShortened) => {
  navigator.clipboard.writeText(urlShortened);
}