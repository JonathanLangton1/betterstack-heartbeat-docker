# Better Stack Heartbeat Script

This is a Python script designed to work with Better Stack's uptime monitoring service. It sends periodic heartbeat requests to maintain the active status of your monitor.

## Features

- Sends a GET request to Better Stack's heartbeat URL every 30 minutes
- Uses environment variables for secure configuration
- Handles exceptions and provides basic logging
- Packaged as a Docker container for easy deployment

## Prerequisites

- Docker
- A Better Stack account with an uptime monitor set up

## Configuration

The script uses the following environment variable:

- `HEARTBEAT_ID`: The unique identifier for your heartbeat monitor from Better Stack

To find your Heartbeat ID:

1. Log in to your Better Stack account
2. Navigate to the Heartbeats section
3. Select the heartbeat you want to use
4. Look for the Heartbeat ID in the provided URL e.g. https://uptime.betterstack.com/api/v1/heartbeat/`HEARTBEAT_ID`

Heartbeat config: Expect a heartbeat every `30 minutes` with a grace period of `5 minutes`

## Usage

1. Clone this repository:

   ```
   git clone https://github.com/JonathanLangton1/betterstack-heartbeat-docker
   cd betterstack-heartbeat-docker
   ```
2. Build the Docker image:

   ```
   docker build -t betterstack-heartbeat .
   ```
3. Run the Docker container:

   ```
   docker run -e HEARTBEAT_ID=your_heartbeat_id betterstack-heartbeat
   ```

   Replace `your_heartbeat_id` with your actual heartbeat ID from Better Stack.

## Docker Compose (optional)

You can also use Docker Compose for easier management. Create a `docker-compose.yml` file with the following content:

```yaml
services:
  heartbeat:
    build: .
    environment:
      - HEARTBEAT_ID=your_heartbeat_id
```

Then run:

```
docker-compose up -d
```

## Logging

The script prints status messages to the console, which can be viewed using Docker logs:

```
docker logs heartbeat
```

## How It Works

The script sends a GET request to `https://uptime.betterstack.com/api/v1/heartbeat/{HEARTBEAT_ID}` every 30 minutes. This regular ping keeps your monitor's status active in Better Stack's uptime monitoring system.

If the script fails to send a heartbeat (due to network issues, for example), it will log the error but continue running, attempting to send the next heartbeat after 30 minutes.

## Troubleshooting

- If you're not seeing heartbeats in your Better Stack dashboard, double-check that your `HEARTBEAT_ID` is correct.
- Ensure your Docker container has internet access to reach the Better Stack API.
- Check the Docker logs for any error messages or exceptions.

## Security Note

Keep your `HEARTBEAT_ID` confidential, as it provides direct access to update your monitor's status.
