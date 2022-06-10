alter table "user" 
alter column password
type varchar(200);

select * from "user";

insert into "user"(id,username, email, password)
values('id','Tuesday', 'tfoleyedwards@gmail.com', 'Allyn');

insert into "bird"(id, common_name, county, state, date)
values('id', 'Vulture', 'Dark Red', 'Misery', '20220601');

insert into "bird"(common_name, latin_name, county, state, date, image, diet, behaviors, conservation)
values('Ruddy Duck', 'Oxyura jamaicensis', 'Marion', 'Indiana', '20220601', 'https://www.allaboutbirds.org/guide/assets/photo/302124271-240px.jpg', 'Aquatic invertebrates', 'Surface Dive', 'Low Concern');

insert into "bird"(common_name, latin_name, county, state, date, image, diet, behaviors, conservation)
values('Western Bluebird', 'Sialia mexicana', 'Lincoln', 'Arizona', '20220501', 'https://www.allaboutbirds.org/guide/assets/photo/67472541-240px.jpg', 'Insects', 'Flycatching', 'Low Concern');

insert into "bird"(common_name, latin_name, county, state, date, image, diet, behaviors, conservation)
values('Western Bluebird', 'Sialia mexicana', 'Lincoln', 'Arizona', '20220501', 'https://www.allaboutbirds.org/guide/assets/photo/67472541-240px.jpg', 'Insects', 'Flycatching', 'Low Concern');

insert into "bird"(common_name, latin_name, county, state, date, image, diet, behaviors, conservation)
values('Prothonotary Warbler', 'Protonotaria citrea', 'Decater', 'Georgia', '20020501', 'https://www.allaboutbirds.org/guide/assets/photo/296766141-240px.jpg', 'Insects', 'Foliage Gleaner', 'Declining');

insert into "bird"(common_name, latin_name, county, state, date, image, diet, behaviors, conservation)
values('Ladder-backed Woodpecker', 'Dryobates scalaris', 'Cimarron', 'Oklahoma', '20210901', 'https://www.allaboutbirds.org/guide/assets/photo/65054631-240px.jpg', 'Insects', 'Bark Forager', 'Low Concern');

insert into "bird"(common_name, latin_name, county, state, date, image, diet, behaviors, conservation)
values('Red-throated Loon', 'Gavia stellata', 'Yakutat', 'Alaska', '20200801', 'https://www.allaboutbirds.org/guide/assets/photo/306758371-240px.jpg', 'Fish', 'Surface Dive', 'Low Concern');

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('American Kestrel', 'Falco sparverius', 'Yamhill', 'Oregon', '20180807', 'https://www.allaboutbirds.org/guide/assets/photo/302366931-240px.jpg', 'Small Mammals', 'Aerial Dive', 'Low Concern', 102);

insert into "bird"(bird_id,common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('bird_id','Snail Kite', 'Rostrhamus sociabilis', 'Dade', 'Florida', '20211207', 'https://www.allaboutbirds.org/guide/assets/photo/305373191-240px.jpg', 'Molluscs', 'Soaring', 'Low Concern', 47);

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('bird_id','Sandhill Crane', 'Antigone canadensis', 'Luce', 'Michigan', '20180107', 'https://www.allaboutbirds.org/guide/assets/photo/303217321-240px.jpg', 'Omnivore', 'Probing', 'Low Concern', 27);

update "bird"
set price = 27.00
where id = 3;




