from neo4j import GraphDatabase


""" make node & relationship"""
def add_article(tx, title, date, media, keyword):
    tx.run("MERGE (a:Article {title: $title , date: $date, media: $media, keyword: $keyword})",
           title=title, date=date, media=media, keyword=keyword)


def add_media(tx):
    tx.run("MATCH (a:Article) "
           "MERGE (b:Media {name:a.media}) "
           "MERGE (a)<-[r:Publish]-(b)")


def add_keyword(tx):
    tx.run("MATCH (a:Article) "
           "UNWIND a.keyword as k "
           "MERGE (b:Keyword {name:k}) "
           "MERGE (a)-[r:Include]->(b)")



""" 한자와 공백 제거 """
# Neo4j -> Gephi 에서 parsing error의 원인이 될 수 있음
def clean_text_for_neo4j(row):
    text = row['title_c']
    text = re.sub(pattern='[^a-zA-Z0-9ㄱ-ㅣ가-힣]', repl='', string=text)
    # print("영어, 숫자, 한글만 포함 : ", text )
    return text

df['title_c_neo4j'] = df.apply(clean_text_for_neo4j, axis=1)



""" 연결 """
# Neo4j 브라우저에서 설정한 계정의 ID, PASSWORD를 통해 접속
greeter = GraphDatabase.driver("bolt://localhost:7687", auth=("dodoria", "sweetapple"))  



""" 입력 """
# Cyper code를 이용,  크롤링한 Data를 DB에 입력
with greeter.session() as session:
    """ make node """
    for idx in range(len(df)):
        session.write_transaction(add_article, title=df.iloc[idx]['title_c_neo4j'], date=df.iloc[idx]['date'],
                                  media=df.iloc[idx]['media'], keyword=list(df.iloc[idx]['keyword']))
    session.write_transaction(add_media)
    session.write_transaction(add_keyword)
