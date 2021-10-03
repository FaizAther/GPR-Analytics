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
    course_id numeric NOT NULL,
    name text NOT NULL,
    manager numeric NOT NULL,
    foreign key (manager) references User(id),
    foreign key (course_id) references Course(id)
);

CREATE TABLE Attendance (
    id numeric PRIMARY KEY,
    event_id numeric,
    name text NOT NULL,
    marker_id numeric NOT NULL,
    student_id numeric NOT NULL,
    startdate date NOT NULL,
    foreign key (event_id) references Event(id),
    foreign key (marker_id) references User(id),
    foreign key (student_id) references User(id)
);

CREATE TABLE Mark (
    attendance_id numeric,
    total numeric, 
    received numeric,
    spec text,
    duedate date,
    foreign key (attendance_id) references Attendance(id)
    primary key (attendance_id, duedate)
);

CREATE TABLE Invite (
    event_id numeric NOT NULL,
    user_id numeric NOT NULL,
    foreign key (event_id) references Event(id),
    foreign key (user_id) references User(id),
    primary key (event_id, user_id)
);
