select *
from bets
where bet_id in (select t1.bet_id
from (select bet_id , count(*) as counter_reg
from bets
group by bet_id) as t1
join (select bet_id , count(*) as counter_more
from bets
where ratio > 2
group by bet_id) as t2
on t1.bet_id = t2.bet_id
where t1.counter_reg = t2.counter_more)
