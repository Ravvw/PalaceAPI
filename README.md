# PalaceAPI
 Palace NFT Marketplace Unofficial API

 Собрал основные методы для работы с t.me/palacenftbot
 Внимание: в данный момент апи, скорее всего, опасно использовать в своих скриптах. Маркет начинает часто сбрасывать токен авторизации без которого апи отвечает ошибкой. Метод update_user_data даёт возможность быстро обновить токен авторизации

 Для начала необходимо установить curl_cffi про помощи pip install curl_cffi

 # check_role
 возвращает "роль" юзера:
 
 {role: <role>} 
 У большинства это будет {role: user}

 # get_commission 
 возвращает комиссию маркетплейса: 
 
 15

 # get_packs(collection_id)
 возвращает паки коллекции по id: 
 
 [{id: <pack_id>, name: <pack_name>, logo: <logo_url>, lottie: <banner_url>}, ...]

# get_offers(collection_id, res_length_limit, offset, sort_type)
возвращает предметы из коллекции, выставленные на продажу

res_length_limit - количество паков в результате

offset - "отступ". при offset 40 будет пропущено 40 первых стоящих на продаже паков

sort_type - например price_asc

{offers: [{id: <offer_id>, price: <price>, token: {"token_id": <collecrion_id>-<pack_id>-<item_id>, pack_id: <pack_id>, instance: <item_id>}}, ...], has_more: <True/False>}


# get_collections 
возвращает доступные коллекции

[{id: <collecrion_id>, name: <collecrion_name>, logo: <logo_url>, cover: <неизвестно>}, ...]

# buy(<offer_id>) 
покупает стикерпак по айди оффера из метода get_offers
