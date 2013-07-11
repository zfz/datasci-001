select sum(doc1.matching_term_count * doc2.matching_term_count)
from
(
    select term, count as matching_term_count
    from frequency
    where docid = '10080_txt_crude'
) doc1 inner join
(
    select term, count as matching_term_count
    from frequency
    where docid = '17035_txt_earn'
) doc2 on doc1.term=doc2.term;
