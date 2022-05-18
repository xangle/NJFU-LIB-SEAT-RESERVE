def _init():
    roomID = {
        '二层A区': 100455344,
        '二层B区': 100455346,
        '三层A区': 100455350,
        '三层B区': 100455352,
        '三层C区': 100455354,
        '四层A区': 100455356,
        '五层A区': 100455358,
        '六层': 100455360,
        '七层北侧': 106658017,
        '三楼夹层': 111488386,
        '四楼夹层': 111488388
    }

    window_seat = {
        '二层A区': [
            '2F-A001',
            '2F-A003',
            '2F-A005',
            '2F-A007',
            '2F-A021',
            '2F-A023',
            '2F-A037',
            '2F-A039',
            '2F-A045',
            '2F-A047',
            '2F-A061',
            '2F-A063',
            '2F-A077',
            '2F-A079',
            '2F-A087',
            '2F-A089',
            '2F-A103',
            '2F-A105',
            '2F-A119',
            '2F-A121',
            '2F-A129',
            '2F-A131',
            '2F-A145',
            '2F-A147',
            '2F-A197',
            '2F-A199',
            '2F-A213',
            '2F-A215',
            '2F-A229',
            '2F-A231',
            '2F-A239',
            '2F-A241',
            '2F-A255',
            '2F-A257',
            '2F-A271',
            '2F-A273',
            '2F-A281',
            '2F-A283',
            '2F-A297',
            '2F-A299',
            '2F-A313',
            '2F-A315',
            '2F-A323',
            '2F-A325',
            '2F-A339',
            '2F-A341',
            '2F-A355',
            '2F-A357',
            '2F-A365',
            '2F-A367',
            '2F-A381',
            '2F-A383',
            '2F-A397',
            '2F-A399',
            '2F-A407',
            '2F-A409',
            '2F-A423',
            '2F-A425'
        ],
        '三层A区': [
            '3F-A001',
            '3F-A003',
            '3F-A005',
            '3F-A007',
            '3F-A009',
            '3F-A011',
            '3F-A013',
            '3F-A015',
            '3F-A017',
            '3F-A019',
            '3F-A021',
            '3F-A023',
            '3F-A025',
            '3F-A027',
            '3F-A029',
            '3F-A031',
            '3F-A135',
            '3F-A137',
            '3F-A139',
            '3F-A141',
            '3F-A143',
            '3F-A145',
            '3F-A147',
            '3F-A149',
            '3F-A151',
            '3F-A153',
            '3F-A155',
            '3F-A157',
            '3F-A159',
            '3F-A161',
            '3F-A163',
            '3F-A165',
            '3F-A167',
            '3F-A169',
            '3F-A171',
            '3F-A173',
            '3F-A175',
            '3F-A177',
            '3F-A179',
            '3F-A181',
            '3F-A183',
            '3F-A185',
            '3F-A187',
            '3F-A207',
            '3F-A209',
            '3F-A223',
            '3F-A225',
            '3F-A233',
            '3F-A235',
            '3F-A249',
            '3F-A251',
            '3F-A265',
            '3F-A267',
            '3F-A275',
            '3F-A277',
            '3F-A291',
            '3F-A293',
            '3F-A307',
            '3F-A309',
            '3F-A317',
            '3F-A319',
            '3F-A333',
            '3F-A335',
            '3F-A349',
            '3F-A351',
            '3F-A359',
            '3F-A361',
            '3F-A375',
            '3F-A377',
            '3F-A391',
            '3F-A393',
            '3F-A401',
            '3F-A403'
        ],
        '四层A区': [
            '4F-A001',
            '4F-A003',
            '4F-A005',
            '4F-A007',
            '4F-A009',
            '4F-A011',
            '4F-A013',
            '4F-A015',
            '4F-A017',
            '4F-A019',
            '4F-A021',
            '4F-A023',
            '4F-A025',
            '4F-A027',
            '4F-A029',
            '4F-A031',
            '4F-A033',
            '4F-A035',
            '4F-A037',
            '4F-A039',
            '4F-A041',
            '4F-A043',
            '4F-A045',
            '4F-A047',
            '4F-A049',
            '4F-A051',
            '4F-A053',
            '4F-A055',
            '4F-A057',
            '4F-A059',
            '4F-A061',
            '4F-A063',
            '4F-A231',
            '4F-A233',
            '4F-A247',
            '4F-A249',
            '4F-A257',
            '4F-A259',
            '4F-A273',
            '4F-A275',
            '4F-A289',
            '4F-A291',
            '4F-A299',
            '4F-A301',
            '4F-A315',
            '4F-A317',
            '4F-A331',
            '4F-A333',
            '4F-A341',
            '4F-A343',
            '4F-A357',
            '4F-A359',
            '4F-A373',
            '4F-A375',
            '4F-A383',
            '4F-A385',
            '4F-A399',
            '4F-A415',
            '4F-A417',
            '4F-A425',
            '4F-A427'
        ],
        '六层': [
            '6F-A001',
            '6F-A003',
            '6F-A005',
            '6F-A007',
            '6F-A009',
            '6F-A011',
            '6F-A013',
            '6F-A015',
            '6F-A017',
            '6F-A019',
            '6F-A021',
            '6F-A023',
            '6F-A025',
            '6F-A027',
            '6F-A029',
            '6F-A031',
            '6F-A033',
            '6F-A035',
            '6F-A037',
            '6F-A039',
            '6F-A041',
            '6F-A043',
            '6F-A045',
            '6F-A047',
            '6F-A121',
            '6F-A123',
            '6F-A125',
            '6F-A127',
            '6F-A129',
            '6F-A131',
            '6F-A133',
            '6F-A135',
            '6F-A137',
            '6F-A139',
            '6F-A141',
            '6F-A143',
            '6F-A145',
            '6F-A147',
            '6F-A149',
            '6F-A151',
            '6F-A153',
            '6F-A155',
            '6F-A157',
            '6F-A159',
            '6F-A161',
            '6F-A163',
            '6F-A165',
            '6F-A167',
            '6F-A169',
            '6F-A171',
            '6F-A173',
            '6F-A175',
            '6F-A297',
            '6F-A299',
            '6F-A301',
            '6F-A303',
            '6F-A305',
            '6F-A307',
            '6F-A309',
            '6F-A311',
            '6F-A313',
            '6F-A315',
            '6F-A317',
            '6F-A319',
            '6F-A321',
            '6F-A323',
            '6F-A325',
            '6F-A327',
            '6F-A329',
            '6F-A331',
            '6F-A333',
            '6F-A335',
            '6F-A337',
            '6F-A339',
            '6F-A341',
            '6F-A343'
        ],
        '三楼夹层': [
            '3FA-001',
            '3FA-003',
            '3FA-005',
            '3FA-007',
            '3FA-009',
            '3FA-011',
            '3FA-013',
            '3FA-015',
            '3FA-017',
            '3FA-019'
        ],
        '四楼夹层': [
            '4FA-001',
            '4FA-003',
            '4FA-005',
            '4FA-007',
            '4FA-009',
            '4FA-011',
            '4FA-013',
            '4FA-015',
            '4FA-017',
            '4FA-019',
            '4FA-021',
            '4FA-023'
        ]
    }

    return roomID, window_seat
