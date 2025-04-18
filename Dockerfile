# Use official Nginx image
FROM nginx:alpine

# Copy static files to Nginx web root
COPY src /usr/share/nginx/html

# Expose port
EXPOSE 80

# Nginx runs by default