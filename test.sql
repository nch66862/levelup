SELECT
    e.id,
    e.name,
    u.id user_id,
    u.first_name || ' ' || u.last_name AS full_name
FROM
    levelupapi_event e
JOIN
    levelupapi_eventattendee ea ON ea.event_id = e.id
JOIN
    levelupapi_gamer gr ON ea.gamer_id = gr.id
JOIN
    auth_user u ON gr.user_id = u.id
