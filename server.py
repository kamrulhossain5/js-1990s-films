from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
import re

app = Flask(__name__)
   
current_id = 30
   
dataset = [{'Id': 1,
  'imdbId': 114709.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114709',
  'Title': 'Toy Story (1995)',
  'Genre': 'Animation|Adventure|Comedy',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMDU2ZWJlMjktMTRhMy00ZTA5LWEzNDgtYmNmZTEwZTViZWJkXkEyXkFqcGdeQXVyNDQ2OTk4MzI@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'John Lasseter',
  'Actors': 'Tom Hanks, Tim Allen, Don Rickles',
  'Runtime (Minutes)': 81.0,
  'Rating': 8.3,
  'Votes': 757074.0,
  'Revenue (Millions)': 333.13,
  'Metascore': 76.0,
  'Summary': "A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room."},
 {'Id': 2,
  'imdbId': 113497.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113497',
  'Title': 'Jumanji (1995)',
  'Genre': 'Action|Adventure|Family',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BZTk2ZmUwYmEtNTcwZS00YmMyLWFkYjMtNTRmZDA3YWExMjc2XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UY268_CR10,0,182,268_AL_.jpg',
  'Director': 'Ridley Scott',
  'Actors': 'Noomi Rapace, Logan Marshall-Green, Michael Fassbender, Charlize Theron',
  'Runtime (Minutes)': 124.0,
  'Rating': 7.0,
  'Votes': 485820.0,
  'Revenue (Millions)': 126.46,
  'Metascore': 65.0,
  'Summary': 'A recovering alcoholic and recently converted Mormon, Arthur "Killer" Kane, of the rock band The New York Dolls, is given a chance at reuniting with his band after 30 years.'},
 {'Id': 3,
  'imdbId': 113228.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113228',
  'Title': 'Grumpier Old Men (1995)',
  'Genre': 'Comedy|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjQxM2YyNjMtZjUxYy00OGYyLTg0MmQtNGE2YzNjYmUyZTY1XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'M. Night Shyamalan',
  'Actors': 'James McAvoy, Anya Taylor-Joy, Haley Lu Richardson, Jessica Sula',
  'Runtime (Minutes)': 117.0,
  'Rating': 7.3,
  'Votes': 157606.0,
  'Revenue (Millions)': 138.12,
  'Metascore': 62.0,
  'Summary': "After everyone is snowed in at the House of Mouse, Mickey suggests they throw their own Christmas party. Everyone is happy, except for Donald who just isn't in to the Christmas spirit. So Mickey shows a series of cartoons that show just what Christmas is all about. It features a star studded cast of Disney characters from everyone's favorite animated Disney movies."},
 {'Id': 4,
  'imdbId': 114885.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114885',
  'Title': 'Waiting to Exhale (1995)',
  'Genre': 'Comedy|Drama|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMTMyMTgyM15BMl5BanBnXkFtZTcwOTc4OTQyMQ@@._V1_UY268_CR4,0,182,268_AL_.jpg',
  'Director': 'Christophe Lourdelet',
  'Actors': 'Matthew McConaughey,Reese Witherspoon, Seth MacFarlane, Scarlett Johansson',
  'Runtime (Minutes)': 108.0,
  'Rating': 7.2,
  'Votes': 60545.0,
  'Revenue (Millions)': 270.32,
  'Metascore': 59.0,
  'Summary': "The villains from the popular animated Disney films are gathered at the House of Mouse with plans to take over. Soon, the villains take over the house and kick out Mickey, Donald and Goofy. It's all up to Mickey and his friends to overthrow evil and return the House of Mouse to normal--or as close to normal as it get's."},
 {'Id': 5,
  'imdbId': 113041.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113041',
  'Title': 'Father of the Bride Part II (1995)',
  'Genre': 'Comedy|Family|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BOTEyNzg5NjYtNDU4OS00MWYxLWJhMTItYWU4NTkyNDBmM2Y0XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'David Ayer',
  'Actors': 'Will Smith, Jared Leto, Margot Robbie, Viola Davis',
  'Runtime (Minutes)': 123.0,
  'Rating': 6.2,
  'Votes': 393727.0,
  'Revenue (Millions)': 325.02,
  'Metascore': 40.0,
  'Summary': 'In the cruel world of junior high, Edwin suffers in a state of anxiety and alienation alongside his only friend, Flake. Misunderstood by their families and demoralized at school daily, their fury simmers quietly until an idea for vengeance offers them a terrifying release. Based on the acclaimed novel "Project X" by Jim Shepard, this unflinching look at adolescence explores how the powerful bonds of childhood friendship and search for belonging can become a matter of life or death.'},
 {'Id': 6,
  'imdbId': 113277.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113277',
  'Title': 'Heat (1995)',
  'Genre': 'Action|Crime|Drama',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNGMwNzUwNjYtZWM5NS00YzMyLWI4NjAtNjM0ZDBiMzE1YWExXkEyXkFqcGdeQXVyNDk3NzU2MTQ@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Yimou Zhang',
  'Actors': 'Matt Damon, Tian Jing, Willem Dafoe, Andy Lau',
  'Runtime (Minutes)': 103.0,
  'Rating': 6.1,
  'Votes': 56036.0,
  'Revenue (Millions)': 45.13,
  'Metascore': 42.0,
  'Summary': "It's a big time in Max's life. He's college bound with his friends and finally free of his embarrassing father as he strives to be a top contender for the X-Games. Unfortunately, Goofy loses his job and learns that he cannot get another job without a college degree. To his son's mortification, Goofy decides to join him in his campus to get that degree. Desperate to distract his father, Max talks him into joining the competing Gamma Fraternity team and introduces him to a wonderful librarian who shares his nostalgic love for 1970's pastimes. Unfortunately, things do not go according to plan as events put this father-son relationship to the test."},
 {'Id': 7,
  'imdbId': 114319.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114319',
  'Title': 'Sabrina (1995)',
  'Genre': 'Comedy|Drama',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTA3OTQ2NTk2ODNeQTJeQWpwZ15BbWU4MDQ3NTM4MDMx._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Damien Chazelle',
  'Actors': 'Ryan Gosling, Emma Stone, Rosemarie DeWitt, J.K. Simmons',
  'Runtime (Minutes)': 128.0,
  'Rating': 8.3,
  'Votes': 258682.0,
  'Revenue (Millions)': 151.06,
  'Metascore': 93.0,
  'Summary': "Based on the books by Beatrix Potter: Peter Rabbit (James Corden;) his three sisters: Flopsy (Margot Robbie,) Mopsy (Elizabeth Debicki) and Cotton Tail (Daisy Ridley) and their cousin Benjamin (Colin Moody) enjoy their days harassing Mr McGregor in his vegetable garden. Until one day he dies and no one can stop them roaming across his house and lands for a full day or so. However, when one of Mr McGregor's relatives inherits the house and goes to check it out, he finds much more than he bargained for. What ensues, is a battle of wills between the new Mr McGregor and the rabbits. But when he starts to fall in love with Bea (Rose Byrne,) a real lover of all nature, his feelings towards them begin to change. But is it too late?"},
 {'Id': 8,
  'imdbId': 114576.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114576',
  'Title': 'Sudden Death (1995)',
  'Genre': 'Action|Crime|Thriller',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BN2NjYWE5NjMtODlmZC00MjJhLWFkZTktYTJlZTI4YjVkMGNmXkEyXkFqcGdeQXVyNDc2NjEyMw@@._V1_UY268_CR0,0,182,268_AL_.jpg',
  'Director': 'James Gray',
  'Actors': 'Charlie Hunnam, Robert Pattinson, Sienna Miller, Tom Holland',
  'Runtime (Minutes)': 141.0,
  'Rating': 7.1,
  'Votes': 7188.0,
  'Revenue (Millions)': 8.01,
  'Metascore': 78.0,
  'Summary': "89 tells the incredible story of one of football's greatest triumphs: when against all odds Arsenal snatched the Championship title from Liverpool at Anfield in the last minute of the last game of the 1988/89 season. It's a universal tale of a band of brothers who, led by a charismatic and deeply respected manager, came together to defy the odds and create history. Mixing archive and previously unseen footage with revealing interviews, insights and memories from the original squad, game officials, famous fans and the people who were there on the night this is the definitive account of a watershed moment in football and a must-watch for any sports fan."},
 {'Id': 9,
  'imdbId': 113189.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113189',
  'Title': 'GoldenEye (1995)',
  'Genre': 'Action|Adventure|Thriller',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMzk2OTg4MTk1NF5BMl5BanBnXkFtZTcwNjExNTgzNA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Morten Tyldum',
  'Actors': 'Jennifer Lawrence, Chris Pratt, Michael Sheen,Laurence Fishburne',
  'Runtime (Minutes)': 116.0,
  'Rating': 7.0,
  'Votes': 192177.0,
  'Revenue (Millions)': 100.01,
  'Metascore': 41.0,
  'Summary': "The illegitimate orphan child, 12-year-old Max, is sold by the local minister for a basket of food to the B枚siger family, who own a mountain farm. Max' initial hope of finally finding a loving home is brutally shattered: The farmer and his wife treat Max like livestock, and their son Jacob humiliates and abuses him. Only the local teacher notices the child suffering on the farm."},
 {'Id': 10,
  'imdbId': 112346.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112346',
  'Title': 'The American President (1995)',
  'Genre': 'Comedy|Drama|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTI5NDU2NDYzOF5BMl5BanBnXkFtZTYwNDk5MDI5._V1_UY268_CR4,0,182,268_AL_.jpg',
  'Director': 'David Yates',
  'Actors': 'Eddie Redmayne, Katherine Waterston, Alison Sudol,Dan Fogler',
  'Runtime (Minutes)': 133.0,
  'Rating': 7.5,
  'Votes': 232072.0,
  'Revenue (Millions)': 234.02,
  'Metascore': 66.0,
  'Summary': 'After being gone for a decade a country star returns home to the love he left behind.'},
 {'Id': 11,
  'imdbId': 112896.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112896',
  'Title': 'Dracula: Dead and Loving It (1995)',
  'Genre': 'Comedy|Fantasy|Horror',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BZWQ0ZDFmYzMtZGMyMi00NmYxLWE0MGYtYzM2ZGNhMTE1NTczL2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMjM5ODMxODc@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Theodore Melfi',
  'Actors': 'Taraji P. Henson, Octavia Spencer, Janelle Monáe,Kevin Costner',
  'Runtime (Minutes)': 127.0,
  'Rating': 7.8,
  'Votes': 93103.0,
  'Revenue (Millions)': 169.27,
  'Metascore': 74.0,
  'Summary': 'Comedian Tom Segura rants about funny things about pop culture and the way of living in 2018.'},
 {'Id': 12,
  'imdbId': 113987.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113987',
  'Title': 'Nixon (1995)',
  'Genre': 'Biography|Drama|History',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNzBlOWY0ZmEtZjdkYS00ZGU0LWEwN2YtYzBkNDM5ZDBjMmI1XkEyXkFqcGdeQXVyMTAwMzUyOTc@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Ron Clements',
  'Actors': "Auli'i Cravalho, Dwayne Johnson, Rachel House, Temuera Morrison",
  'Runtime (Minutes)': 107.0,
  'Rating': 7.7,
  'Votes': 118151.0,
  'Revenue (Millions)': 248.75,
  'Metascore': 81.0,
  'Summary': 'Nothing is impossible for a group of young campers, friends and enemies alike, on a weekend retreat at Camp Pinnacle. But what starts as an exciting wilderness adventure turns into trouble when a young camper goes missing and the rest of the group must set out to find him. The campers are forced to overcome their differences and band together to re-claim their weekend and make it out of the woods before dark!'},
 {'Id': 13,
  'imdbId': 112760.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112760',
  'Title': 'Cutthroat Island (1995)',
  'Genre': 'Action|Adventure|Comedy',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMDg2YTI0YmQtYzgwMi00Zjk4LWJkZjgtYjg0ZDE2ODUzY2RlL2ltYWdlXkEyXkFqcGdeQXVyNjQzNDI3NzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Nacho Vigalondo',
  'Actors': 'Anne Hathaway, Jason Sudeikis, Austin Stowell,Tim Blake Nelson',
  'Runtime (Minutes)': 109.0,
  'Rating': 6.4,
  'Votes': 8612.0,
  'Revenue (Millions)': 2.87,
  'Metascore': 70.0,
  'Summary': 'Adam unexpectedly visits his family house at Christmas after a few years of working abroad. No family member knows about his secret plans and the real reasons of his visit.'},
 {'Id': 14,
  'imdbId': 112641.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112641',
  'Title': 'Casino (1995)',
  'Genre': 'Crime|Drama',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTcxOWYzNDYtYmM4YS00N2NkLTk0NTAtNjg1ODgwZjAxYzI3XkEyXkFqcGdeQXVyNTA4NzY1MzY@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Chris Renaud',
  'Actors': 'Louis C.K., Eric Stonestreet, Kevin Hart, Lake Bell',
  'Runtime (Minutes)': 87.0,
  'Rating': 6.6,
  'Votes': 120259.0,
  'Revenue (Millions)': 368.31,
  'Metascore': 61.0,
  'Summary': 'Task Force X targets a powerful mystical object that they will risk their lives to steal.'},
 {'Id': 15,
  'imdbId': 114388.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114388',
  'Title': 'Sense and Sensibility (1995)',
  'Genre': 'Drama|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNzk1MjU3MDQyMl5BMl5BanBnXkFtZTcwNjc1OTM2MQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Mel Gibson',
  'Actors': 'Andrew Garfield, Sam Worthington, Luke Bracey,Teresa Palmer',
  'Runtime (Minutes)': 139.0,
  'Rating': 8.2,
  'Votes': 211760.0,
  'Revenue (Millions)': 67.12,
  'Metascore': 71.0,
  'Summary': "Anna spends her entire childhood under the care of a mysterious man she only knows as Daddy. He keeps her locked in an attic making her fear the Wildling, a child-eating monster that roams the outside. At age 16, Anna is freed by small-town sheriff Ellen Cooper who helps her start a new life as a normal teenager. But as Anna's body begins to blossom, her childhood nightmares return with a vengeance, leading to the conclusion of a terrifying secret."},
 {'Id': 16,
  'imdbId': 113101.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113101',
  'Title': 'Four Rooms (1995)',
  'Genre': 'Comedy',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNDc3Y2YwMjUtYzlkMi00MTljLTg1ZGMtYzUwODljZTI1OTZjXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Paul Greengrass',
  'Actors': 'Matt Damon, Tommy Lee Jones, Alicia Vikander,Vincent Cassel',
  'Runtime (Minutes)': 123.0,
  'Rating': 6.7,
  'Votes': 150823.0,
  'Revenue (Millions)': 162.16,
  'Metascore': 58.0,
  'Summary': 'A dystopian thriller set in the year 2030 that sees the world in a permanent state of economic recession and facing serious environmental problems as a result of global warming.'},
 {'Id': 17,
  'imdbId': 113845.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113845',
  'Title': 'Money Train (1995)',
  'Genre': 'Action|Comedy|Crime',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNDEwNzcyNjkzNl5BMl5BanBnXkFtZTcwNzQyMzYxMQ@@._V1_UY268_CR4,0,182,268_AL_.jpg',
  'Director': 'Denis Villeneuve',
  'Actors': 'Amy Adams, Jeremy Renner, Forest Whitaker,Michael Stuhlbarg',
  'Runtime (Minutes)': 116.0,
  'Rating': 8.0,
  'Votes': 340798.0,
  'Revenue (Millions)': 100.5,
  'Metascore': 81.0,
  'Summary': 'Irene must endure 2 weeks of community service at a retirement home. Following her passion for cheerleading, she secretly signs up the senior residents to audition for a dance-themed reality show to prove that you don\'t need to be physically "perfect" to be perfectly AWESOME.'},
 {'Id': 18,
  'imdbId': 113161.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113161',
  'Title': 'Get Shorty (1995)',
  'Genre': 'Comedy|Crime|Thriller',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMjAwODYzNDY4Ml5BMl5BanBnXkFtZTcwODkwNTgzNA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Stephen Gaghan',
  'Actors': 'Matthew McConaughey, Edgar Ramírez, Bryce Dallas Howard, Corey Stoll',
  'Runtime (Minutes)': 120.0,
  'Rating': 6.7,
  'Votes': 19053.0,
  'Revenue (Millions)': 7.22,
  'Metascore': 49.0,
  'Summary': "The mysteries surrounding her father's death in the Vietnam war lead ultra-endurance mountain biker Rebecca Rusch on an emotional journey as she pedals 1200 miles of the Ho Chi Minh trail."},
 {'Id': 19,
  'imdbId': 112722.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112722',
  'Title': 'Copycat (1995)',
  'Genre': 'Crime|Drama|Mystery',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BYWUwNDk2ZDYtNmFkMi00NjE5LWE1M2ItYTRkNTFjZDU3ZDU4L2ltYWdlL2ltYWdlXkEyXkFqcGdeQXVyMTYxNjkxOQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Kenneth Lonergan',
  'Actors': 'Casey Affleck, Michelle Williams, Kyle Chandler,Lucas Hedges',
  'Runtime (Minutes)': 137.0,
  'Rating': 7.9,
  'Votes': 134213.0,
  'Revenue (Millions)': 47.7,
  'Metascore': 96.0,
  'Summary': 'A look at the life and career of professional wrestler Andr茅 Roussimoff, who gained notoriety in the 1980s as Andre the Giant.'},
 {'Id': 20,
  'imdbId': 114168.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114168',
  'Title': 'Powder (1995)',
  'Genre': 'Drama|Fantasy|Mystery',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTM2NDczNjYwMV5BMl5BanBnXkFtZTYwNTI3Mjc4._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Walt Dohrn',
  'Actors': 'Anna Kendrick, Justin Timberlake,Zooey Deschanel, Christopher Mintz-Plasse',
  'Runtime (Minutes)': 92.0,
  'Rating': 6.5,
  'Votes': 38552.0,
  'Revenue (Millions)': 153.69,
  'Metascore': 56.0,
  'Summary': 'Bjarke Ingels started out as a young man dreaming of creating cartoons. Now, he has been named "one of architecture\'s biggest innovators" by The Wall Street Journal and one of The 100 Most Influential People on the planet by TIME Magazine. BIG TIME follows Bjarke during the course of 7 years (2009-2016), while he struggles to finish his biggest project so far. We are let into Bjarke\'s creative processes as well as the endless compromises that his work entails, and we are on the side when his personal life starts putting pressure on him, too. In addition to the recently opened architectural marvel VIA 57 West (625 West 57th Street), Bjarke Ingels\' company Bjarke Ingels Group (BIG) was given the task of designing and building one of the skyscrapers which will replace Two World Trade Center in Manhattan. While Bjarke is creating these buildings, which will change the New York skyline, he is hit by health-related issues. The Film offers an intimate look into the innovative and ambitious ...'},
 {'Id': 21,
  'imdbId': 113627.0,
  'Imdb Link': 'http://www.imdb.com/title/tt113627',
  'Title': 'Leaving Las Vegas (1995)',
  'Genre': 'Drama|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BNDg3MDM5NTI0MF5BMl5BanBnXkFtZTcwNDY0NDk0NA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Roland Emmerich',
  'Actors': 'Liam Hemsworth, Jeff Goldblum, Bill Pullman,Maika Monroe',
  'Runtime (Minutes)': 120.0,
  'Rating': 5.3,
  'Votes': 127553.0,
  'Revenue (Millions)': 103.14,
  'Metascore': 32.0,
  'Summary': 'Two teen rival babysitters, Jenny and Lola, team up to hunt down one of their kids who accidentally runs away into the big city without any supervision.'},
 {'Id': 22,
  'imdbId': 112682.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112682',
  'Title': 'The City of Lost Children (1995)',
  'Genre': 'Fantasy|Sci-Fi',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BZGQxZDMwYzYtYmFjNi00NWYyLThjZjAtMDJhODZhYTkyZDNhXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_UY268_CR7,0,182,268_AL_.jpg',
  'Director': 'Jon Lucas',
  'Actors': 'Mila Kunis, Kathryn Hahn, Kristen Bell,Christina Applegate',
  'Runtime (Minutes)': 100.0,
  'Rating': 6.2,
  'Votes': 66540.0,
  'Revenue (Millions)': 113.08,
  'Metascore': 60.0,
  'Summary': "A gritty L.A crime saga which follows the intersecting and often personally connected lives of an elite unit of the LA County Sheriff's Dept. and the state's most successful bank robbery crew as the outlaws plan a seemingly impossible heist on the Federal Reserve Bank of downtown Los Angeles."},
 {'Id': 23,
  'imdbId': 115012.0,
  'Imdb Link': 'http://www.imdb.com/title/tt115012',
  'Title': 'Yao a yao, yao dao wai po qiao (1995)',
  'Genre': 'Crime|Drama|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTgyMzAwOTQyNF5BMl5BanBnXkFtZTcwNDU1MjgxMQ@@._V1_UY268_CR1,0,182,268_AL_.jpg',
  'Director': 'Justin Kurzel',
  'Actors': 'Michael Fassbender, Marion Cotillard, Jeremy Irons,Brendan Gleeson',
  'Runtime (Minutes)': 115.0,
  'Rating': 5.9,
  'Votes': 112813.0,
  'Revenue (Millions)': 54.65,
  'Metascore': 36.0,
  'Summary': 'The son (Lee Jong-Suk) of a high-ranking North Korean official is suspected of committing serial murders around the world. To stop the killer, South Korea, North Korea and Interpol chase after him.'},
 {'Id': 24,
  'imdbId': 112792.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112792',
  'Title': 'Dangerous Minds (1995)',
  'Genre': 'Biography|Drama',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BZjk2YjNkYTYtOTZkNy00ZmRkLWI5ODEtYzA4MTM3MzMyZjhlXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'John Hamburg',
  'Actors': 'Zoey Deutch, James Franco, Tangie Ambrose,Cedric the Entertainer',
  'Runtime (Minutes)': 111.0,
  'Rating': 6.3,
  'Votes': 48123.0,
  'Revenue (Millions)': 60.31,
  'Metascore': 39.0,
  'Summary': "The up-and-down-and-up-again story of musician Dewey Cox, whose songs would change a nation. On his rock 'n roll spiral, Cox sleeps with 411 women, marries three times, has 36 kids, stars in his own 70s TV show, collects friends ranging from Elvis to the Beatles to a chimp, and gets addicted to - and then kicks - every drug known to man; but despite it all, Cox grows into a national icon and eventually earns the love of a good woman - longtime backup singer Darlene."},
 {'Id': 25,
  'imdbId': 114746.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114746',
  'Title': 'Twelve Monkeys (1995)',
  'Genre': 'Mystery|Sci-Fi|Thriller',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BN2Y2OWU4MWMtNmIyMy00YzMyLWI0Y2ItMTcyZDc3MTdmZDU4XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Terry Gilliam',
  'Actors': 'Bruce Willis, Madeleine Stowe, Brad Pitt',
  'Runtime (Minutes)': 129.0,
  'Rating': 7.5,
  'Votes': 126030.0,
  'Revenue (Millions)': 10.64,
  'Metascore': 67.0,
  'Summary': "In a future world devastated by disease, a convict is sent back in time to gather information about the man-made virus that wiped out most of the human population on the planet."},
 {'Id': 26,
  'imdbId': 114952.0,
  'Imdb Link': 'http://www.imdb.com/title/tt114952',
  'Title': 'Wings of Courage (1995)',
  'Genre': 'Adventure|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTc3ODY1MjA3OF5BMl5BanBnXkFtZTcwODgzOTgyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Bryan Singer',
  'Actors': 'James McAvoy, Michael Fassbender, Jennifer Lawrence, Nicholas Hoult',
  'Runtime (Minutes)': 144.0,
  'Rating': 7.1,
  'Votes': 275510.0,
  'Revenue (Millions)': 155.33,
  'Metascore': 52.0,
  'Summary': 'In the same night that happens a blood red moon, some longtime friends reunite to dinner: the group is formed by plastic surgeon Alfonso and his wife, psychologist Eva, who are the hosts of the dinner; lawyers Antonio and his wife Ana; taxi driver Eduardo and his young and recent wife, veterinary Blanca; and finally Pepe, a former gym teacher actually unemployed, who surprisingly appears without Luc铆a, his recent girlfriend. Motivated by Blanca, who have some suspects about the group by the behaviors of some of them, she proposes a game where all diners leave their cell phones on the table, at the condition to say to everyone the contents of all text and voice messages. Starting like an innocent game, the progressive revelation of secrets as they appear cause a series the events each time more dramatics: Alfonso suspects that Eva has an affair, Ana thinks wrongly that Antonio is homosexual, Blanca realizes a horrible side about her marriage with Eduardo, and Pepe tries to keep hidden ...'},
 {'Id': 27,
  'imdbId': 112431.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112431',
  'Title': 'Babe (1995)',
  'Genre': 'Comedy|Drama|Family',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BYjg4ZjUzMzMtYzlmYi00YTcwLTlkOWUtYWFmY2RhNjliODQzXkEyXkFqcGdeQXVyNTUyMzE4Mzg@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Tim Miller',
  'Actors': 'Ryan Reynolds, Morena Baccarin, T.J. Miller, Ed Skrein',
  'Runtime (Minutes)': 108.0,
  'Rating': 8.0,
  'Votes': 627797.0,
  'Revenue (Millions)': 363.02,
  'Metascore': 65.0,
  'Summary': "The film centers on Joe Paterno, who, after becoming the winningest coach in college football history, is embroiled in Penn State's Jerry Sandusky sexual abuse scandal, challenging his legacy and forcing him to face questions of institutional failure regarding the victims."},
 {'Id': 28,
  'imdbId': 112637.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112637',
  'Title': 'Carrington (1995)',
  'Genre': 'Biography|Drama|Romance',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BZjQ3MTBkNDEtMGRlZS00OTY0LTkzYjktOWU2MzI3ZDRiMjY5XkEyXkFqcGdeQXVyMTA0MjU0Ng@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Paul W.S. Anderson',
  'Actors': 'Milla Jovovich, Iain Glen, Ali Larter, Shawn Roberts',
  'Runtime (Minutes)': 107.0,
  'Rating': 5.6,
  'Votes': 46165.0,
  'Revenue (Millions)': 26.84,
  'Metascore': 49.0,
  'Summary': "13 of Edward Hopper's paintings are brought alive by the film, telling the story of a woman, whose thoughts, emotions and contemplations let us observe an era in American history. Shirley is a woman in America in the 1930s, '40s, '50s, and early '60s. A woman who would like to influence the course of history with her professional and socio political involvement."},
 {'Id': 29,
  'imdbId': 112818.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112818',
  'Title': 'Dead Man Walking (1995)',
  'Genre': 'Crime|Drama',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BMTM3NzA1MjM2N15BMl5BanBnXkFtZTcwMzY3MTMzNA@@._V1_UX182_CR0,0,182,268_AL_.jpg',
  'Director': 'Anthony Russo',
  'Actors': 'Chris Evans, Robert Downey Jr.,Scarlett Johansson, Sebastian Stan',
  'Runtime (Minutes)': 147.0,
  'Rating': 7.9,
  'Votes': 411656.0,
  'Revenue (Millions)': 408.08,
  'Metascore': 75.0,
  'Summary': "Takaki and Akari are two classmates in elementary school. During their time together they have become close friends. Their relationship is tested when Akari moves to another city because of her parents' jobs. Both of them struggle to keep their friendship alive, as time and distance slowly pulls them apart. When Takaki finds out that he is moving further away, he decides to visit Akari one last time."},
 {'Id': 30,
  'imdbId': 112286.0,
  'Imdb Link': 'http://www.imdb.com/title/tt112286',
  'Title': 'Across the Sea of Time (1995)',
  'Genre': 'Adventure|Drama|Family',
  'Poster': 'https://images-na.ssl-images-amazon.com/images/M/MV5BOTIwMzk1MDc1MF5BMl5BanBnXkFtZTcwMTEzNDkyMQ@@._V1_UY268_CR43,0,182,268_AL_.jpg',
  'Director': 'Christopher Nolan',
  'Actors': 'Matthew McConaughey, Anne Hathaway, Jessica Chastain, Mackenzie Foy',
  'Runtime (Minutes)': 169.0,
  'Rating': 8.6,
  'Votes': 1047747.0,
  'Revenue (Millions)': 187.99,
  'Metascore': 74.0,
  'Summary': "Agnes Varda, one of the leading lights of France's honored French New Wave cinema era, and professional photographer and muralist, J.R., partake on a special art project. Together, they travel around France in a special box truck equipped as a portable photo booth and traveling printing facility as they take photographs of people around the country. With that inspiration, they also create special colossal mural pictures of individuals, communities and places they want to honor and celebrate. Along the way, the old cinematic veteran and the young artistic idealist enjoy an odd friendship as they chat and explore their views on the world as only they can."}
]
  
@app.route('/')
def index(name=None):
    return render_template('layout.html', name=name)

@app.route('/init', methods=['GET', 'POST'])
def init():  
    global dataset
    
#     json_data = request.get_json()
#     print("json_data : " + str(json_data))
    return jsonify(dataset = dataset)

@app.route('/add_item', methods=['GET', 'POST'])
def add_item():   
    return render_template('add_item.html')

@app.route('/add_entry', methods=['GET', 'POST'])
def add_entry():
    global current_id
    global dataset
    
    data_entry = {}
    form_data = request.get_json()
#     print(form_data)
    current_id+=1
    data_entry["Id"] = current_id
    for value in form_data:
        data_entry[value["name"]] = value["value"]  
#     print(data_entry)

    dataset.append(data_entry)
    print(dataset)
#     render_template('view_item.html')
    return jsonify(Id = current_id)
#     return render_template('view_item.html')
    
@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/search_input', methods=['GET', 'POST'])
def search_input():
    global current_id
    global dataset
    
#     data_entry = {}
    result = []
    input = request.get_json()
    print("input: "+str(input))
    pattern = re.compile(input, re.I)
    for i in dataset:
        for j in i.values():
#             print("j:"+str(j))
            if re.search(pattern, str(j)):
                result.append(i)
                break
#     print("result: ")
#     print(result)
    return jsonify(result = result)

@app.route('/delete_item', methods=['GET', 'POST'])
def delete_item():
    global dataset
    global current_id
    
    input = request.get_json()
#     print(json_data)
    if input <= current_id :
        del dataset[input]['Rating']
        current_id -= 1
    return jsonify(result = dataset, current_id = current_id)

@app.route('/view', methods=['GET', 'POST'])
def view_item():
    return render_template('view_item.html')

@app.route('/view/<item_id>', methods=['GET', 'POST'])
def view(item_id=None):
    global dataset
    
    item = dataset[int(item_id)-1]

    return render_template('item.html', item = item)

@app.route('/add_rating', methods = ['GET', 'POST'])
def add_rating():
    json_data = request.get_json()
    id = json_data["Id"]
    rating = json_data["rating"]
    for i in range(len(dataset)):
        if i == id:
            item = dataset[i]
            dataset[i]["Rating"].append(rating)
    return jsonify(item = item)

if __name__ == '__main__':
   app.run(debug = True)
   
  