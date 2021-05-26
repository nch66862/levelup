CREATE VIEW GAMES_BY_USER AS
SELECT
    g.id,
    g.title,
    g.maker,
    g.gametype_id,
    g.number_of_players,
    g.skill_level,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_game g
JOIN
    levelupapi_gamer gr ON g.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
;
CREATE VIEW EVENTS_BY_USER AS
SELECT
    e.id as event_id,
    e.event_time,
    e.location,
    e.name as event_name,
    g.title as game_name,
    gr.id gamer_id,
    u.id as user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_event e
JOIN
    levelupapi_eventattendee ea ON ea.event_id = e.id
JOIN
    levelupapi_gamer gr ON ea.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
JOIN
    levelupapi_game g ON g.id = e.game_id;
