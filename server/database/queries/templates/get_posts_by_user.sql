SELECT *
FROM posts
LEFT OUTER JOIN image_posts ON image_posts.post_id = posts.id
LEFT OUTER JOIN discuss_posts ON discuss_posts.post_id = posts.id
WHERE posts.uploader_id = :user_id AND posts.type = :type
ORDER BY posts.time DESC
OFFSET :offset
LIMIT :limit;
