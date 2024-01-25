#GymGenius - Your Ultimate Fitness Companion
GymGenius is a comprehensive fitness website that offers a collection of over 1300 sports exercises sourced from a meticulously curated dataset obtained from the internet. The platform aims to empower users with a wealth of exercise options to make their fitness journey more enjoyable and effective.

Key Features:
1. Exercise Database and ETL Process
Leveraging a robust Extract, Transform, Load (ETL) process, GymGenius efficiently processes the dataset information, storing it in an SQLite database for seamless access and retrieval.
2. Nutrition Calculator
GymGenius provides a built-in Nutrition Calculator powered by an API, enabling users to make informed dietary choices tailored to their fitness goals.
3. Popularity Tracking and Analysis
Every user interaction, such as clicks on exercises, is tracked to determine popularity. GymGenius utilizes AWS DynamoDB to store this data and employs Spark for insightful analytics, helping identify the top 10 most popular exercises.
4. AWS EC2 Instance Deployment
The platform is deployed on an AWS EC2 instance running Linux, ensuring reliability, scalability, and accessibility.
Getting Started
To experience the power of GymGenius, follow these steps:

Clone the repository.
Set up the SQLite database by running the provided ETL scripts.
Deploy the application on an AWS EC2 instance following the provided instructions.
Start exploring a vast array of exercises and utilizing the Nutrition Calculator for a holistic fitness experience.
Vision
GymGenius aspires to create a user-friendly environment, encouraging individuals to embark on their fitness journey with confidence, whether they are beginners or seasoned fitness enthusiasts. The platform aims to bridge the gap between users and expert-level workout routines, making fitness more accessible to everyone.


