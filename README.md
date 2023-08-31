# Visualizing Data in Football

1. [Overview](#overview)
2. [Analysis](#analysis)
3. [Inferences & Conclusion](#inferences-and-conclusion)
4. [References](#references)

## Overview
I embarked on an intriguing data exploration project, analyzing a comprehensive dataset from Kaggle with international football match data spanning from 1872 to 2022. Using Python, I prepared and cleaned the data to ensure accurate results.

With a sharp eye for detail, I identified and analyzed interesting patterns and trends within the dataset, providing valuable insights into the world of international football.

To make the data more engaging, I used visualization techniques, creating clear and compelling representations of the trends. The final output painted a vivid picture of the sport's evolution over the years, offering valuable perspectives for enthusiasts and analysts alike.

![Alt Text](https://images.pexels.com/photos/1884574/pexels-photo-1884574.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1)

## Analysis
We used python libraries such as (numpy and pandas) to clean and process our [dataset]("https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017") before we dive into our analysis. 

For our analysis, we merge the available datasets and further filter and select data from the following tournaments :
- FIFA World Cup
- Copa America
- African Cup of Nations
- UEFA Euro
- AFC Asian Cup

**How have the number of goals scored across various editions varied?**
  
![goals_across_decades](https://github.com/Hamza-149/visualizing-data-in-football/assets/69048367/12480220-c74f-470b-82bf-0ee3371d0e99)
We understand that this fluctuaton can be due to teams adpoting different styles of play and how trends kept changing over years. This is mainly due to the evolution of formations over time and different styles of play being adopted.

- **How many teams have won the respective tournaments?**

![most_decorated_countries](https://github.com/Hamza-149/visualizing-data-in-football/assets/69048367/6e61f5b6-2008-4a77-ad66-03e75bc8f7b3)
![most_decorated_countries_matplotlib](https://github.com/Hamza-149/visualizing-data-in-football/assets/69048367/76445c94-867d-4b0c-a3c1-117c757dd85f)

**Brazil**, **Germany** and **Italy** have dominated both the International and the Continental tournaments, whilst countries such as **Egypt**, **Cameroon**, **Ghana**, **Ivory Coast**, **Nigeria**, **Spain**, **Argentina** and **Uruguay** have enjoyed quite a lot of Continental success.

Now that we have visualized the winners from the top 5 major international tournaments, let us go one step further and see how many of these champions were victors on home soil.

**How many of these champions were hosts when they won the respective tournaments?**

![trophies_won_as_hosts](https://github.com/Hamza-149/visualizing-data-in-football/assets/69048367/46ce2fa4-5560-48ab-9e45-abc47ad0c271)

There have been a fair few victors who were hosts as well but there seem to be quite a lot that weren't necessaily hosting tournaments which they won, with _Copa América_ being an exception. Let's get a more specific visualisation as to how often do we see _Host Nations_ come out on top.

**What is the percentage of teams that have won the tournament whilst hosting it?**

![percentage_of_tournaments_won_by_hosts](https://github.com/Hamza-149/visualizing-data-in-football/assets/69048367/3551ea1d-8052-4d5d-acd1-38e54e83fc8d)

Here we can see that **FIFA World Cup**, **African Cup of Nations** and **UEFA Euro** have a decent (but not so encouraging) win percentage whilst being the Home Team whereas in **Copa América** the Home Team seems to have a higher success rate.

## _Inferences and Conclusion_
We can conculde by saying that although being the Host Nation may hold an advantage, it doesn't necessarily guarantee 100% success. There is a lot of other data that can contribute to a team's result such as tactics, formation, team chemistry, etc.

## _References_
- The [*dataset*](https://www.kaggle.com/datasets/martj42/international-football-results-from-1872-to-2017) we used for our analysis was obtained from [*Kaggle*](https://www.kaggle.com/).
- To clean some of our data that we extracted from kaggle we cross-referenced it with the data available on Wikipedia.
