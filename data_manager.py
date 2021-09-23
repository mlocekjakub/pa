import connection


# Write the first 10 letters next to each other
# Clicking on letters load shows starting with that letter that has more than 20 episodes
# title, year, episode count, actor count
# Page mustn’t reload (so you have to do it with fetch)

@connection.connection_handler
def get_shows_by_letter(cursor, letter):
    query = f"""
    SELECT s.title, s.year, COUNT(e.id) as episode_count
    FROM shows s
    JOIN seasons se ON s.id = se.show_id
    JOIN episodes e ON se.id = e.season_id
    WHERE s.title LIKE '{letter}%'
    GROUP BY s.id, s.title, year
    having COUNT(e.id) > 20"""
    cursor.execute(query)
    return cursor.fetchall()
