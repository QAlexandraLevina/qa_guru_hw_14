# <img src='icons_and_img/baze_rp.png' width="30" height="30"/> BAZE RP Website Autotests
Проект по автоматизации веб-сайта BAZE RP с использованием Python, Pytest, Selene, Allure, Jenkins, Selenoid.

---
## 📋 О проекте

---
Данный проект представляет собой фреймворк для UI-тестирования веб-сайта '[BAZE RP](https://bazerp.com/)'.

---
## 🛠️ Технологии и инструменты

---
<img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original-wordmark.svg' width="70" height="70"/> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg' width="70" height="70"/> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original-wordmark.svg' width="70" height="70"/> <img src='https://img.icons8.com/stickers/100/selenium-test-automation.png' width="70" height="70"/> <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg' width="70" height="70"/> <img src='https://avatars.githubusercontent.com/u/5879127?s=200&v=4' width="70" height="70"/> <img src='icons_and_img/Allure_Report.svg' width="70" height="70"/> <img src='icons_and_img/Selenoid.svg' width="70" height="70"/> <img src='https://img.icons8.com/color/144/telegram-app--v1.png' width="70" height="70"/>

---
## 🔍 Область тестирования

---
Охватывает смоук и регрессионные сценарии для тестов: 

- Header - проверка 'шапки' сайта на всех страницах для авторизованного и неавторизованного пользователя.

- Footer - проверка 'подвала' сайта на всех страницах.

- Раздел 'Ключевые особенности' - валидация контента и его функциональности.

- Навигация - клик по кнопке 'Начать игру' с переходом в раздел 'Как начать играть' и проверкой ссылок.

- Авторизация - позитивная проверка входа в аккаунт.

---
### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg' width="20" height="20"/> Запуск тестов локально

---
**1.** Клонирование репозитория:

`git clone https://github.com/QAlexandraLevina/qa_guru_hw_14.git`

**2.** Установка зависимостей:

`pip install -r requirements.txt`

**3.** Запуск стабильных тестов с генерацией отчёта Allure:

`pytest --ignore=baze/tests_unstable/ --alluredir=reports/allure-results`

**4.** Просмотр Allure отчёта:

`allure serve reports/allure-results`

---
### <img src='https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-original.svg' width="20" height="20"/> Запуск тестов на удалённом сервере Jenkins

---
**1.** Авторизоваться в '[Jenkins](https://jenkins.autotests.cloud/)'.

**2.** Перейти в Джобу: `test_jenkins_qa_guru_homework_14`.
<img src='icons_and_img/search_job.png' width="900" height="800"/>

**3.** Нажать 'Build with Parameters' на панели слева для запуска тестов.
<img src='icons_and_img/build_now.png' width="900" height="800"/>

**4.** После завершения сборки открыть Allure-отчёт, кликнув на соответствующую иконку:
<img src='icons_and_img/Allure_Report.svg' width="20" height="20"/>
<img src='icons_and_img/report_icon.png' width="900" height="800"/>

---
### 📊 Визуализация отчётов с результатами (Allure Report, Telegram)

---
#### **Allure Report**
<img src='icons_and_img/allure_report_page.png' width="900" height="800"/>

#### **Telegram Notifications**
<img src='icons_and_img/telegram_notification.png' width="350" height="300"/>