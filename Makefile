deploy:
	hugo && rsync -avz --delete public/ aisa:~/public_html/ib002/

.PHONY: deploy
