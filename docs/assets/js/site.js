const menu = document.querySelector('.menu-toggle');
const links = document.getElementById('myLinks');
menu.addEventListener('click', () => {
  const open = menu.getAttribute('aria-expanded') !== 'true';
  menu.setAttribute('aria-expanded', String(open));
  menu.setAttribute('aria-label', open ? 'Close navigation' : 'Open navigation');
  links.classList.toggle('open', open);
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape' && menu.getAttribute('aria-expanded') === 'true') {
    menu.setAttribute('aria-expanded', 'false');
    menu.setAttribute('aria-label', 'Open navigation');
    links.classList.remove('open');
    menu.focus();
  }
});
const newsButton = document.querySelector('.news-toggle button');
if (newsButton) {
  newsButton.addEventListener('click', () => {
    const open = newsButton.getAttribute('aria-expanded') !== 'true';
    newsButton.setAttribute('aria-expanded', String(open));
    document.getElementById('older-news').hidden = !open;
    newsButton.textContent = open ? 'Show less' : 'Show more';
  });
}
