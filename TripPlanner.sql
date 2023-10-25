CREATE DATABASE TripPlanner;

USE TripPlanner;

CREATE TABLE User (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(255) NOT NULL
    -- other fields as necessary
);

CREATE TABLE Trip (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    start_date DATE,
    end_date DATE,
    destination VARCHAR(255),
    trip_type ENUM('family', 'friends', 'backpack'),
    theme ENUM('adventure', 'holiday', 'spiritual'),
    staying_preference TEXT,
    dietary_preference TEXT,
    cost_parameter ENUM('cheap', 'budget', 'luxury'),
    FOREIGN KEY (user_id) REFERENCES User(id)
);

CREATE TABLE Activity (
    id INT AUTO_INCREMENT PRIMARY KEY,
    trip_id INT,
    activity_name VARCHAR(255),
    start_time TIME,
    end_time TIME,
    status ENUM('pending', 'completed', 'in_progress'),
    FOREIGN KEY (trip_id) REFERENCES Trip(id)
);
