-- Comments

CREATE TABLE User (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    password text NOT NULL
);

CREATE TABLE University (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    admin numeric NOT NULL,
    foreign key (admin) references User(id)
);

CREATE TABLE Faculty (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    university numeric NOT NULL,
    dean numeric NOT NULL,
    foreign key (university) references University(id),
    foreign key (dean) references User(id)
);

CREATE TABLE Course (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    coordinator numeric NOT NULL, 
    foreign key (coordinator) references User(id)
);

CREATE TABLE Event (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    manager numeric NOT NULL, 
    foreign key (manager) references User(id)
);

CREATE TABLE Attendance (
    id numeric PRIMARY KEY,
    name text NOT NULL,
    authority numeric NOT NULL,
    foreign key (authority) references User(id)
);

CREATE TABLE EventTicket (
    event_id numeric NOT NULL,
    user_id numeric NOT NULL,
    foreign key (event_id) references Event(id),
    foreign key (user_id) references User(id),
    primary key (event_id, user_id)
);
