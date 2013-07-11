-- select docid, sum(count) from frequency where term in ('washington', 'taxes', 'treasury') group by docid order by sum(count) desc limit 5;

select max(k) from (select sum(count)  as k from frequency where term in ('washington', 'taxes', 'treasury') group by docid order by sum(count) desc);
