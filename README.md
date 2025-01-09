# OpenAI API Docker Image

This repository contains the Dockerfile and scripts to build a Docker image to use the OpenAI API.

## Dependencies

- Docker
- Docker compose

## Requirements

To use this Docker image, you need an OpenAI API key. Here are the steps to get one:

1. Go to [platform.openai.com/settings/profile/api-keys](https://platform.openai.com/settings/profile/api-keys)
2. Click the Create a new secret key button
3. Name it “Docker CLI” (or whatever you’d like)
4. Copy and save the API key for use with the CLI

## Usage

1. Clone this repository
2. Create a `.env` file with the following content:
   ```
   OPENAI_API_KEY=<YOUR_API_KEY>
   MODEL=<MODEL> # e.g. "gpt-4o"
   PRE_PROMPT=<PRE_PROMPT> # e.g. "Translate the following text to French:"
   TEMPERATURE=<TEMPERATURE> # e.g. 1
   MAX_TOKENS=<MAX_TOKENS> # e.g. 150
   ```
3. Build the Docker image: `docker compose build`
4. Run the Docker container: `PROMPT="a prompt" docker compose up`
5. You can create a function  in a .bash_aliases file to make it easier to run the container:
    ````bash
    chatgpt() {
      local path_to_docker_compose="$HOME/Projects/Docker-OpenAI-API/docker-compose.yml"
      local prompt="$1"

      PROMPT="$prompt" docker compose -f "$path_to_docker_compose" up
    }
   ```
