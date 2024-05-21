use master;

create database DatabaseRacingGame;
use DatabaseRacingGame;

drop database DatabaseRacingGame;

create table Item(
	item_ID char(3) primary key,
	item_Name varchar(20),
	item_Cost int
);

create table Player(
	player_User varchar(20) primary key,
	player_Password  varchar(50),
	player_Name varchar(20),
	player_Point int
);

create table Player_Item(
	item_ID char(3) foreign key references Item(item_ID),
	player_User varchar(20) foreign key references Player(player_User),
	PRIMARY KEY (item_ID, player_User)
);

insert into Item values('001', 'Star', 2200);
insert into Item values('002', 'Heart', 2500);
insert into Item values('003', 'SpainFlag', 3000);
insert into Item values('004', 'VietNamFlag', 3000);
insert into Item values('005', 'SouthKoreaFlag', 3000);
insert into Item values('006', 'JapanFlag', 3000);
insert into Item values('007', 'ChinaFlag', 3000);
insert into Item values('008', 'USAFlag', 3000);
insert into Item values('009', 'EnglandFlag', 3000);
insert into Item values('010', 'NoelHat', 2500);
insert into Item values('011', 'PharaohHat', 2500);
insert into Item values('012', 'PartyHat', 2500);
insert into Item values('013', 'ChefHat', 2500);
insert into Item values('014', 'PilotHat', 2500);
insert into Item values('015', 'Fire', 2300);
insert into Item values('016', 'Lightning', 2400);
insert into Item values('017', 'BatmanLogo', 2500);
insert into Item values('018', 'Shield', 2500);

insert into Player values('user001', '123456', 'Quang Trung', 0);

insert into Player_Item values('004', 'user001');

select * from Item;
select * from Player;
Select * from Player_Item;