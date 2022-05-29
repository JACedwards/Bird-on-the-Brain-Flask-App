alter table "user" 
alter column password
type varchar(200);

select * from "user";

insert into "user"(id,username, email, password)
values('id','Tuesday', 'tfoleyedwards@gmail.com', 'Allyn');