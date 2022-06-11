alter table "user" 
alter column password
type varchar(200);

select * from "bird";

insert into "user"(id,username, email, password)
values('id','Tuesday', 'tfoleyedwards@gmail.com', 'Allyn');

insert into "bird"(id, common_name, county, state, date)
values('id', 'Vulture', 'Dark Red', 'Misery', '20220601');

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('8','Ruddy Duck', 'Oxyura jamaicensis', 'Marion', 'Indiana', '20220601', 'https://www.allaboutbirds.org/guide/assets/photo/302124271-240px.jpg', 'Aquatic invertebrates', 'Surface Dive', 'Low Concern', 88);


insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('7','Western Bluebird', 'Sialia mexicana', 'Lincoln', 'Arizona', '20220501', 'https://www.allaboutbirds.org/guide/assets/photo/67472541-240px.jpg', 'Insects', 'Flycatching', 'Low Concern', 53);

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('6','Prothonotary Warbler', 'Protonotaria citrea', 'Decater', 'Georgia', '20020501', 'https://www.allaboutbirds.org/guide/assets/photo/296766141-240px.jpg', 'Insects', 'Foliage Gleaner', 'Declining', 16);

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('5','Ladder-backed Woodpecker', 'Dryobates scalaris', 'Cimarron', 'Oklahoma', '20210901', 'https://www.allaboutbirds.org/guide/assets/photo/65054631-240px.jpg', 'Insects', 'Bark Forager', 'Low Concern', 13);

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('4','Red-throated Loon', 'Gavia stellata', 'Yakutat', 'Alaska', '20200801', 'https://www.allaboutbirds.org/guide/assets/photo/306758371-240px.jpg', 'Fish', 'Surface Dive', 'Low Concern', 73);

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('3','American Kestrel', 'Falco sparverius', 'Yamhill', 'Oregon', '20180807', 'https://www.allaboutbirds.org/guide/assets/photo/302366931-240px.jpg', 'Small Mammals', 'Aerial Dive', 'Low Concern', 102);

insert into "bird"(bird_id,common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('2','Snail Kite', 'Rostrhamus sociabilis', 'Dade', 'Florida', '20211207', 'https://www.allaboutbirds.org/guide/assets/photo/305373191-240px.jpg', 'Molluscs', 'Soaring', 'Low Concern', 47);

insert into "bird"(bird_id, common_name, latin_name, county, state, date, image, diet, behaviors, conservation, price)
values('1','Sandhill Crane', 'Antigone canadensis', 'Luce', 'Michigan', '20180107', 'https://www.allaboutbirds.org/guide/assets/photo/303217321-240px.jpg', 'Omnivore', 'Probing', 'Low Concern', 27);

update "bird"
set bird_id = 1
where bird_id = 'bird_id';

select * from "bird";




