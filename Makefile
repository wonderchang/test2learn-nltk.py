TEST ?=

project_name = test2learn-python-nltk
workspace = $(PWD)

image = $(project_name)
network = $(project_name)

corenlp_image = nlpbox/corenlp:2018-10-27
corenlp_container = $(project_name)-stanford-corenlp
corenlp_port = 9000

build:
	docker build -t $(image) .
	docker run --rm --tty --detach \
		--name $(corenlp_container) \
		--publish $(corenlp_port):$(corenlp_port) \
		$(corenlp_image)
	docker network create $(network)
	docker network connect $(network) $(corenlp_container)

define docker_run
	docker run --rm --interactive --tty \
		--volume $(workspace):/workspace \
		--network $(network) \
		--env PYTHONDONTWRITEBYTECODE=1 \
		--env TEST=$(TEST) \
		--env CORENLP_HOST=$(corenlp_container):$(corenlp_port) \
		$(image) $(1)
endef

shell:
	$(call docker_run,/bin/bash)

test:
	$(call docker_run,tox)

clean:
	docker rm -f $(corenlp_container)
	docker rmi -f $(image) $(corenlp_image)
	docker network rm $(network)
