import json

def get_dirs_of_responses_list_format_from_json(json_file_path):
    # open json in json_object variable
    with open(json_file_path) as json_file:
        json_object = json.load(json_file)
        json_file.close()

    url_mockss = json_object[1:]
    urls = []
    mocks = []
    api_apiCallNResponses = []
    apis = []
    apiCall_responses = []
    responses = []

    for e in url_mockss:
        mocks.append(e["mocks"])
        # print(mocks,end="\n\n")
    e=mocks[2]
    # print('\n\n')
    # print(e[1])
    # print(len(mocks))
    # print("\n\n\n")

    for mock in mocks:
        #contains pce
        # print(mock)
        mock_pce = mock[0]
        api = mock_pce[0]
        apiCall_responses = mock_pce[1]
        for apiCall_responses in apiCall_responses:
            responses.append(apiCall_responses['response'])
            # print(apiCall_responses['response'])
        #pce and wdh
        if len(mock) == 2:
            mock_wdh = mock[1]
            api = mock_wdh[0]
            apiCall_responses = mock_wdh[1]
            for apiCall_responses in apiCall_responses:
                responses.append(apiCall_responses['response'])
                # print(apiCall_responses['response'])
            pass
        
    return responses
    # for e in mocks:
    #     print("\n\n")
    #     print(f'len de e[0] :{len(e[0])}')
    #     print(f'len de e[0][1] :{len(e[0][1])}')
    #     print(f'len de e[0][1][0] :{len(e[0][1][0])}')
        
    #     print(e[0][1][0])
    #     if len(e) == 2:
    #         print(f'len de e[1] :{len(e[1])}')
    #         print(f'len de e[1][1] :{len(e[1][1])}')
    #         print(f'len de e[1][1][0] :{len(e[1][1][0])}')
    #         print(e[1][1][0])
    #     if len(e) == 3:
    #         print("hahaha")

    # for e in mocks:
    #     responses.append(e[0][1][0]['response'])
    #     if len(e) == 1:
    #         print("len 1")
    #         print(e[0][1][0]['response'])        
    #     if len(e) == 2:
    #         print("len 2")
    #         responses.append(e[1][1][0]['response'])
    #         print(e[1][1][0]['response'])
    # for e in responses:
    #     print(e)

json_file_path = "C:\\Users\\aymane.dassouli\\Desktop\\mission\\PCE\\client\\cypress\\fixtures\\url-apiCalls.json"

get_dirs_of_responses_list_format_from_json(json_file_path)
