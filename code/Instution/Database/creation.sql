-- Comments
CREATE TABLE User (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    password text NOT NULL
);

CREATE TABLE Course (
    id numeric,
    foreign key (id) references User(id),
    primary key (id) 
);