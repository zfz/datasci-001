select count(*) from (
    (
        select docid from Frequency where term='transactions'
    )
    join
    (
        select docid from Frequency where term='world'
    )
    using (docid)
);

-- same as the followings:
-- select count(*) from (
--     (
--         select docid from Frequency where term='transactions'
--     ) as d1
--     join
--     (
--         select docid from Frequency where term='world'
--     ) as d2
--     on d1.docid=d2.docid
-- );
