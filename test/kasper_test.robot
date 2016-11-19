*** Settings ***

Library  Selenium2Library
Library  ../pages/MainPage.py
Library  ../pages/ProfilePage.py
Library  ../pages/ProductPage.py
Library     OperatingSystem



Suite Setup    Start tests
Suite Teardown	 Close Browser

*** Variables ***

| ${VALID KIS DATA} |    3 devices 1 year 79.95
| ${VALID KIS TAB} |    Kaspersky Internet Security

| ${VALID KAV DATA} |    1 device 1 year 39.95
| ${VALID KAV TAB} |    Kaspersky Anti-Virus

| ${VALID KTS DATA} |    1 device 1 year 79.95
| ${VALID KTS TAB} |    Kaspersky Total Security


${VALID EMAIL}   wpi69397@xzsok.com
${VALID PASSWORD}   wpi69397@xzsok.comQ
${VALID TABLE TITLE}   Windows


*** Test Cases ***
Test authorization
    Authorization should be successful with ${json}

Test move to the tab
    Tab shop should be open

Test product
    [Template]   The product data with ${VALID KIS TITLE} must be equal ${VALID DATA}
    ${VALID KIS TAB}     ${VALID KIS DATA}
    ${VALID KAV TAB}     ${VALID KAV DATA}
    ${VALID KTS TAB}     ${VALID KTS DATA}


*** Keywords ***
Start tests
    ${file}=   Get File     TEST_DATA.json
    ${json}=    evaluate    json.loads('''${file}''')    json
    set suite variable    ${json}
    Open Browser      ${json['VALID BASE URL']}
    Maximize Browser Window

Authorization should be with ${json}
    ${user_header} =    login      ${json[]}    ${VALID PASSWORD}
    Should Be Equal   ${VALID EMAIL}      ${user_header}

Tab shop should be open
    ${header} =     top_menu
    Should Be Equal    ${VALID TABLE TITLE}     ${header}

The product data with ${VALID KIS TITLE} must be equal ${VALID DATA}
    ${result} =    check_product       ${VALID KIS TITLE}
    Should Be Equal    ${VALID DATA}     ${result}