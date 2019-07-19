history = { 
    'user1':
    ['google.com','teachbase.ru'],
    'user2': 
    ['yandex.ru','teachbase.ru'],
    'user3':
    ['google.com','youtube.com','mail.ru'],
    'user4': 
    ['google.com', 'stackoverflow.com', 'python.org']
}

def calculate_hits(history):
    hits = {}
    for users, urls in history.items():
        for websites in urls:
            website_counter = hits.get(websites)
            if website_counter is None:
                hits[websites] = 1
            else:
                hits[websites] = website_counter + 1
    print(hits)

calculate_hits(history)

