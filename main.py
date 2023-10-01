from selenium.webdriver import Firefox, FirefoxOptions
from selenium.webdriver.common.by import By
import wget


def extrair_perfil(driver: Firefox, url: str):
    driver.get(url)

    driver.implicitly_wait(4)

    elem = driver.find_element(By.CSS_SELECTOR, 'section.x1qjc9v5 h2') # changed!
    name = elem.text

    elems = driver.find_elements(By.CSS_SELECTOR, 'section ul.x78zum5.x1q0g3np.xieb3on li span._ac2a span')
    posts = elems[0].text
    seguidores = elems[1].text
    seguindo = elems[2].text

    elem = driver.find_element(By.CSS_SELECTOR, 'section div.x7a106z')
    bio = elem.text

    elem = driver.find_element(By.CSS_SELECTOR, 'img.xpdipgo') # changed
    img = elem.get_attribute('src')

    print(f'Name: {name}\nImg: {img[:len(img)//2]}\nPosts: {posts} | Followers: {seguidores} | Following: {seguindo}\nBio:\n{bio}')
    
    wget.download(img, 'images/') # salva dentro da pasta `images`


def pegar_comentarios_post(driver: Firefox, url: str):
    driver.get(url)
    driver.implicitly_wait(7)

    elem = driver.find_element(By.CSS_SELECTOR, 'div._aagu div._aagv img')
    img = elem.get_attribute('src')

    # Comments
    elems = driver.find_elements(By.CSS_SELECTOR, 'ul._a9ym div.x1qjc9v5 li._a9zj._a9zl div._a9zm')
    for e in elems:
        try:
            # Acontece porque quando nao ha likes, havera somente 'Reply' no comentario
            likes = e.find_element(By.CSS_SELECTOR, 'button._a9ze span').text
            if 'Reply' in likes:
                likes = 0
            else:
                likes = int(likes.split(' ')[0])
        except:
            likes = 0

        comentario = {
            'foto': e.find_element(By.CSS_SELECTOR, 'img').get_attribute('src')[:10],
            'nome': e.find_element(By.CSS_SELECTOR, 'h3._a9zc').text,
            'texto': e.find_element(By.CSS_SELECTOR, 'div._a9zs').text,
            'likes': likes
        }
        print(comentario)

    print(f'Img: {img[:len(img)//3]}')


options = FirefoxOptions()
#options.add_argument('-headless')
driver = Firefox(options=options)

url_perfil = 'https://www.instagram.com/bbcbrasil/'
extrair_perfil(driver, url_perfil)

#url_post = 'https://www.instagram.com/p/CxzGr_4Oe97/?utm_source=ig_web_copy_link&igshid=MzRlODBiNWFlZA=='
#get_post_metadata(driver, url_post)

input('\nAperte qualquer tecla para fechar...')
driver.close()