create table x(
    row_num int,
    col_num int,
    value int,
    primary key(row_num, col_num)
);

create table y(
    row_num int,
    col_num int,
    value int,
    primary key(row_num, col_num)
);

insert into x select * from a where row_num=2;
insert into y select * from b where col_num=3;

select sum(x.value * y.value) from x,y where (x.col_num = y.row_num);

drop table x;
drop table y;
