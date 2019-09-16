# 2019 Kakao Blind Recruitment - 6

import re
# from bs4 import BeautifulSoup

pages = [
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>",
    "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"
]

# meta_parser = re.compile('<meta(.*?)/>', re.DOTALL).findall(pages[0])

# soup = BeautifulSoup(pages[0], 'lxml')
# meta_parser = soup.find('meta')
# print(type(meta_parser.attrs))
# print(meta_parser.attrs)

print()
print(pages)
print(len(pages))
print(pages[0])
print()

html = []
body_list = []

for i in range(len(pages)):
    html = pages[i].split('\n')
    # html.append(pages[i].split('\n'))
    print()
    print(html)
    print(len(html))

    start = 0
    end = 0

    # HTML <body> 태그 안 포함된 내용만 추출
    for j in range(len(html)):
        if html[j] == '<body>':
            start = j + 1
            # print(start)

        elif html[j] == '</body>':
            end = j
            # print(start)
            # print(end)
            body = html[start:end]
            print(body)
            # body.append(html[start:end])

    if body:
        body_list.append(body)

print()
# print(body_list)

body_text = []
link_cnt = []
a = []

punctuations = ',.'

# HTML <body> 태그 내에 존재하는 문장을 하나의 문장으로 통합
for i in range(len(body_list)):

    line = ''
    cnt = 0

    for j in range(len(body_list[i])):
        # 태그 <a>를 포함하지 않는 행
        if not body_list[i][j].startswith('<a'):
            print(i, j, end=' ')
            print(body_list[i][j])

            line += body_list[i][j]

        # 태그 <a>를 포함하는 행
        else:
            print(i, j, end=' ')
            print(body_list[i][j])

            cnt += 1

    print(i, "문장", line)
    print(i, "%d번 웹페이지 <body>" % (i + 1), end=' ')
    print("외부 링크 (<a>)의 수:", cnt)
    print()

    body_text.append(line)
    link_cnt.append(cnt)

# 단어에 포함되어 있는 특수문자 제거
for i in range(len(body_text)):
    for str in body_text[i]:
        if str in punctuations:
            body_text[i] = body_text[i].replace(str, '')
            # print(body_text[i])

    if punctuations not in body_text[i]:
        print(body_text[i])

print()
print(body_text, '\n')

# 기본점수 구하기
key = 'blind'
print("word:", key)

word_cnt = []

for i in range(len(body_text)):
    word = body_text[i].split(' ')
    print(word)

    # 검색어 일치 횟수
    cnt = 0

    for j in range(len(word)):
        cnt += word[j].lower().count(key)

    print("검색어 등장 횟수:", cnt)

    word_cnt.append(cnt)

print()
# print("각 웹페이지의 검색어 등장 횟수:", word_cnt)
# print("각 웹페이지의 외부 참조 링크 수:", link_cnt)

# cnt = [[word_cnt[i], link_cnt[i]] for i in range(len(word_cnt))]
cnt = [tuple([word_cnt[i], link_cnt[i]]) for i in range(len(word_cnt))]
# print(cnt)

web = ['a', 'b', 'c']

web_info = [[web[i], cnt[i]] for i in range(len(web))]
print("각 웹페이지의 검색어 등장 횟수, 외부 링크 수:", web_info)

ini_score = [[web[i], word_cnt[i]] for i in range(len(web))]
print("각 웹페이지의 기본 점수", ini_score)

link_score = [[web[i], word_cnt[i] / link_cnt[i]] for i in range(len(web))]
print("각 웹페이지의 링크 점수", link_score)

a_parser = []

for page in pages:
    a = re.compile('<a href="(.*?)">', re.DOTALL).findall(page)
    a_parser.append(a)

print(a_parser)

link_ref = [[web[i], a_parser[i]] for i in range(len(web))]
print("각 웹페이지의 참조 외부 링크:", link_ref)

for web in link_ref:
    # print(web)
    for i in range(len(web[1])):
        print(web[1][i])
        ref = re.compile('https://(.*?).com', re.DOTALL).findall(web[1][i])
        print(ref)




match_score = []

print(ini_score[0][1] + link_score[1][1] + link_score[2][1])
print(ini_score[1][1] + link_score[0][1])
print(ini_score[1][1] + link_score[1][1])


'''
answer = 0
meta_parser = re.compile('<meta(.+?)/>')
a_parser = re.compile('<a(.+?)>')
page_infos = []

for page in pages:
    page_dict = dict()
    a_tags = a_parser.findall(page)
    # print(a_tags)

    outer_url = []

    for a_tag in a_tags:
        first_idx = end_idx = -1

        for idx, char in enumerate(a_tag):
            if char == '"':
                if first_idx == -1:
                    first_idx = idx
                    # print(first_idx)

                elif end_idx == -1:\
                    end_idx = idx
                    # print(end_idx)

        outer_url.append(a_tag[first_idx+1:end_idx])
        # print(outer_url)

    meta_tag = meta_parser.search(page).group()
    content_prop = meta_tag.split(' ')[2]
    first_idx = end_idx = -1

    for idx, char in enumerate(content_prop):
        if char == '"':
            if first_idx == -1:
                first_idx = idx

            elif end_idx == -1:
                end_idx = idx

    url = content_prop[first_idx+1: end_idx]
    page_dict['outer_url_list'] = outer_url
    page_dict['url'] = url
    page_dict['keyword_point'] = re.sub('[^a-z]+', '.', page.lower()).split('.').count(word.lower())
    page_dict['link_point'] = 0
    page_infos.append(page_dict)

for page_info in page_infos:
    for outer_url in page_info['outer_url_list']:
        for outer_url_page_candidate in page_infos:
            if outer_url == outer_url_page_candidate['url']:
                outer_url_page_candidate['link_point'] += page_info['keyword_point']/len(page_info['outer_url_list'])

point_lst = [page_info['keyword_point'] + page_info['link_point'] for page_info in page_infos]
print(point_lst)
print(point_lst.index(max(point_lst)))
'''
