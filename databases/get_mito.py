#!/usr/bin/python
from Bio import SeqIO

mitolist = ['EG_transcript_10014','EG_transcript_10079','EG_transcript_10083','EG_transcript_10100','EG_transcript_10115','EG_transcript_10161','EG_transcript_10179','EG_transcript_10184','EG_transcript_10201','EG_transcript_10254','EG_transcript_10283','EG_transcript_10302','EG_transcript_10307','EG_transcript_10370','EG_transcript_10379','EG_transcript_10443','EG_transcript_10458','EG_transcript_10476','EG_transcript_10588','EG_transcript_10591','EG_transcript_10613','EG_transcript_10620','EG_transcript_10635','EG_transcript_10682','EG_transcript_10720','EG_transcript_10758','EG_transcript_10767','EG_transcript_10773','EG_transcript_10778','EG_transcript_10824','EG_transcript_10828','EG_transcript_1083','EG_transcript_10875','EG_transcript_10882','EG_transcript_10912','EG_transcript_10923','EG_transcript_10937','EG_transcript_1094','EG_transcript_10979','EG_transcript_11072','EG_transcript_11150','EG_transcript_11180','EG_transcript_11184','EG_transcript_11187','EG_transcript_11225','EG_transcript_11317','EG_transcript_11341','EG_transcript_11415','EG_transcript_11456','EG_transcript_11471','EG_transcript_11505','EG_transcript_11544','EG_transcript_11556','EG_transcript_11568','EG_transcript_11577','EG_transcript_11597','EG_transcript_11617','EG_transcript_11626','EG_transcript_1163','EG_transcript_11701','EG_transcript_11730','EG_transcript_11734','EG_transcript_11739','EG_transcript_1176','EG_transcript_1177','EG_transcript_11779','EG_transcript_11827','EG_transcript_11845','EG_transcript_11908','EG_transcript_11934','EG_transcript_11950','EG_transcript_11957','EG_transcript_11996','EG_transcript_12052','EG_transcript_1206','EG_transcript_12101','EG_transcript_12133','EG_transcript_12184','EG_transcript_12212','EG_transcript_12231','EG_transcript_12268','EG_transcript_12294','EG_transcript_12306','EG_transcript_12354','EG_transcript_12368','EG_transcript_12415','EG_transcript_12418','EG_transcript_12422','EG_transcript_12438','EG_transcript_12447','EG_transcript_1245','EG_transcript_12467','EG_transcript_12469','EG_transcript_12472','EG_transcript_12480','EG_transcript_12497','EG_transcript_12535','EG_transcript_12536','EG_transcript_1255','EG_transcript_12631','EG_transcript_12637','EG_transcript_12655','EG_transcript_12664','EG_transcript_12671','EG_transcript_12737','EG_transcript_12763','EG_transcript_12805','EG_transcript_12861','EG_transcript_12862','EG_transcript_12885','EG_transcript_12890','EG_transcript_12902','EG_transcript_12961','EG_transcript_12972','EG_transcript_12986','EG_transcript_12997','EG_transcript_13053','EG_transcript_13172','EG_transcript_13173','EG_transcript_13179','EG_transcript_13213','EG_transcript_13256','EG_transcript_13259','EG_transcript_1326','EG_transcript_1329','EG_transcript_13311','EG_transcript_13352','EG_transcript_13361','EG_transcript_13401','EG_transcript_13431','EG_transcript_13438','EG_transcript_13449','EG_transcript_13463','EG_transcript_13467','EG_transcript_13468','EG_transcript_13473','EG_transcript_1348','EG_transcript_13483','EG_transcript_13498','EG_transcript_13531','EG_transcript_13548','EG_transcript_13551','EG_transcript_13555','EG_transcript_13564','EG_transcript_13592','EG_transcript_13595','EG_transcript_13668','EG_transcript_1368','EG_transcript_13753','EG_transcript_13767','EG_transcript_13792','EG_transcript_13795','EG_transcript_13805','EG_transcript_13823','EG_transcript_13830','EG_transcript_13840','EG_transcript_13843','EG_transcript_13898','EG_transcript_13899','EG_transcript_13905','EG_transcript_13947','EG_transcript_13951','EG_transcript_13957','EG_transcript_13959','EG_transcript_13992','EG_transcript_13997','EG_transcript_13998','EG_transcript_14092','EG_transcript_14094','EG_transcript_14099','EG_transcript_14120','EG_transcript_14139','EG_transcript_14146','EG_transcript_14195','EG_transcript_14216','EG_transcript_14237','EG_transcript_14243','EG_transcript_14263','EG_transcript_14273','EG_transcript_14279','EG_transcript_1428','EG_transcript_14288','EG_transcript_14338','EG_transcript_14349','EG_transcript_14381','EG_transcript_14391','EG_transcript_14422','EG_transcript_14424','EG_transcript_14473','EG_transcript_14495','EG_transcript_14515','EG_transcript_14523','EG_transcript_14545','EG_transcript_14563','EG_transcript_14568','EG_transcript_14580','EG_transcript_14625','EG_transcript_14637','EG_transcript_14638','EG_transcript_14649','EG_transcript_14823','EG_transcript_14837','EG_transcript_14859','EG_transcript_14863','EG_transcript_14864','EG_transcript_14868','EG_transcript_1490','EG_transcript_14917','EG_transcript_14923','EG_transcript_14931','EG_transcript_14945','EG_transcript_14958','EG_transcript_1497','EG_transcript_14985','EG_transcript_14995','EG_transcript_15039','EG_transcript_15045','EG_transcript_15055','EG_transcript_15065','EG_transcript_15075','EG_transcript_15105','EG_transcript_15122','EG_transcript_15128','EG_transcript_15139','EG_transcript_15154','EG_transcript_15185','EG_transcript_15209','EG_transcript_15244','EG_transcript_15319','EG_transcript_15330','EG_transcript_15350','EG_transcript_15398','EG_transcript_15401','EG_transcript_15411','EG_transcript_15419','EG_transcript_15457','EG_transcript_15475','EG_transcript_1548','EG_transcript_15492','EG_transcript_1556','EG_transcript_15577','EG_transcript_15615','EG_transcript_15625','EG_transcript_15660','EG_transcript_15674','EG_transcript_15712','EG_transcript_15718','EG_transcript_15735','EG_transcript_15742','EG_transcript_15794','EG_transcript_15810','EG_transcript_15845','EG_transcript_15849','EG_transcript_159','EG_transcript_1590','EG_transcript_15919','EG_transcript_15922','EG_transcript_15958','EG_transcript_15998','EG_transcript_16003','EG_transcript_16008','EG_transcript_16019','EG_transcript_16038','EG_transcript_16043','EG_transcript_16062','EG_transcript_16084','EG_transcript_16116','EG_transcript_16160','EG_transcript_16177','EG_transcript_16185','EG_transcript_16224','EG_transcript_16231','EG_transcript_16245','EG_transcript_16257','EG_transcript_16359','EG_transcript_16371','EG_transcript_16382','EG_transcript_1640','EG_transcript_16482','EG_transcript_1653','EG_transcript_16534','EG_transcript_1654','EG_transcript_16588','EG_transcript_16593','EG_transcript_1661','EG_transcript_1663','EG_transcript_16635','EG_transcript_16639','EG_transcript_1666','EG_transcript_16724','EG_transcript_16761','EG_transcript_16863','EG_transcript_1687','EG_transcript_16893','EG_transcript_16898','EG_transcript_16945','EG_transcript_17061','EG_transcript_1707','EG_transcript_17090','EG_transcript_17096','EG_transcript_17106','EG_transcript_17132','EG_transcript_17164','EG_transcript_17195','EG_transcript_17240','EG_transcript_17241','EG_transcript_17323','EG_transcript_17348','EG_transcript_17372','EG_transcript_17379','EG_transcript_17401','EG_transcript_17405','EG_transcript_17406','EG_transcript_17408','EG_transcript_17460','EG_transcript_17507','EG_transcript_17527','EG_transcript_17535','EG_transcript_17619','EG_transcript_17654','EG_transcript_17692','EG_transcript_17694','EG_transcript_17713','EG_transcript_17727','EG_transcript_17744','EG_transcript_17752','EG_transcript_17771','EG_transcript_17772','EG_transcript_17874','EG_transcript_17899','EG_transcript_17968','EG_transcript_17989','EG_transcript_18070','EG_transcript_18103','EG_transcript_18109','EG_transcript_18133','EG_transcript_18134','EG_transcript_18138','EG_transcript_18154','EG_transcript_18179','EG_transcript_18180','EG_transcript_1819','EG_transcript_18209','EG_transcript_18240','EG_transcript_18250','EG_transcript_18305','EG_transcript_18315','EG_transcript_18355','EG_transcript_18376','EG_transcript_18414','EG_transcript_18452','EG_transcript_18464','EG_transcript_18473','EG_transcript_18488','EG_transcript_1850','EG_transcript_1851','EG_transcript_18536','EG_transcript_18565','EG_transcript_18631','EG_transcript_18667','EG_transcript_1869','EG_transcript_18691','EG_transcript_18707','EG_transcript_18727','EG_transcript_18732','EG_transcript_18745','EG_transcript_18767','EG_transcript_18769','EG_transcript_1878','EG_transcript_18807','EG_transcript_18811','EG_transcript_18872','EG_transcript_18880','EG_transcript_18919','EG_transcript_18963','EG_transcript_18974','EG_transcript_18998','EG_transcript_19016','EG_transcript_19151','EG_transcript_19156','EG_transcript_19235','EG_transcript_19289','EG_transcript_19329','EG_transcript_19336','EG_transcript_19356','EG_transcript_19403','EG_transcript_19472','EG_transcript_19495','EG_transcript_1951','EG_transcript_19555','EG_transcript_19566','EG_transcript_19609','EG_transcript_19629','EG_transcript_19650','EG_transcript_19675','EG_transcript_19677','EG_transcript_19704','EG_transcript_19719','EG_transcript_19736','EG_transcript_19795','EG_transcript_19796','EG_transcript_19809','EG_transcript_19831','EG_transcript_19840','EG_transcript_19861','EG_transcript_19893','EG_transcript_19911','EG_transcript_19995','EG_transcript_20044','EG_transcript_2009','EG_transcript_20108','EG_transcript_20144','EG_transcript_20149','EG_transcript_20226','EG_transcript_20340','EG_transcript_20363','EG_transcript_20381','EG_transcript_20430','EG_transcript_20434','EG_transcript_20451','EG_transcript_20462','EG_transcript_20467','EG_transcript_20497','EG_transcript_2055','EG_transcript_20636','EG_transcript_20705','EG_transcript_20806','EG_transcript_20828','EG_transcript_20934','EG_transcript_2099','EG_transcript_21','EG_transcript_21115','EG_transcript_21118','EG_transcript_21133','EG_transcript_21146','EG_transcript_21234','EG_transcript_21237','EG_transcript_21271','EG_transcript_2131','EG_transcript_21310','EG_transcript_21325','EG_transcript_21350','EG_transcript_21390','EG_transcript_21444','EG_transcript_21457','EG_transcript_21477','EG_transcript_21478','EG_transcript_21494','EG_transcript_21511','EG_transcript_21522','EG_transcript_21579','EG_transcript_21628','EG_transcript_21706','EG_transcript_21707','EG_transcript_21720','EG_transcript_21763','EG_transcript_21796','EG_transcript_21797','EG_transcript_21879','EG_transcript_21906','EG_transcript_22015','EG_transcript_22072','EG_transcript_22093','EG_transcript_22111','EG_transcript_22169','EG_transcript_22173','EG_transcript_22270','EG_transcript_22314','EG_transcript_22381','EG_transcript_22409','EG_transcript_22412','EG_transcript_22423','EG_transcript_22468','EG_transcript_22485','EG_transcript_22493','EG_transcript_22507','EG_transcript_22602','EG_transcript_22722','EG_transcript_22752','EG_transcript_22846','EG_transcript_2288','EG_transcript_22899','EG_transcript_22952','EG_transcript_22967','EG_transcript_23105','EG_transcript_23194','EG_transcript_23248','EG_transcript_23304','EG_transcript_23305','EG_transcript_23359','EG_transcript_23401','EG_transcript_2342','EG_transcript_23431','EG_transcript_23438','EG_transcript_23444','EG_transcript_23553','EG_transcript_23615','EG_transcript_23644','EG_transcript_23774','EG_transcript_23810','EG_transcript_23844','EG_transcript_239','EG_transcript_23935','EG_transcript_23941','EG_transcript_23963','EG_transcript_23983','EG_transcript_24','EG_transcript_24035','EG_transcript_24149','EG_transcript_2419','EG_transcript_24207','EG_transcript_24213','EG_transcript_24328','EG_transcript_24417','EG_transcript_24503','EG_transcript_24541','EG_transcript_24560','EG_transcript_24567','EG_transcript_24589','EG_transcript_24607','EG_transcript_24608','EG_transcript_24689','EG_transcript_24718','EG_transcript_24767','EG_transcript_2480','EG_transcript_24803','EG_transcript_24856','EG_transcript_2487','EG_transcript_24888','EG_transcript_24920','EG_transcript_2494','EG_transcript_24975','EG_transcript_25116','EG_transcript_25197','EG_transcript_25233','EG_transcript_2525','EG_transcript_25308','EG_transcript_25318','EG_transcript_25320','EG_transcript_2535','EG_transcript_25374','EG_transcript_25404','EG_transcript_25414','EG_transcript_2545','EG_transcript_2549','EG_transcript_25501','EG_transcript_2552','EG_transcript_25604','EG_transcript_25617','EG_transcript_2563','EG_transcript_25719','EG_transcript_25720','EG_transcript_25802','EG_transcript_26051','EG_transcript_26059','EG_transcript_26065','EG_transcript_2608','EG_transcript_26084','EG_transcript_26116','EG_transcript_26148','EG_transcript_26151','EG_transcript_26203','EG_transcript_26207','EG_transcript_2622','EG_transcript_2632','EG_transcript_2633','EG_transcript_26376','EG_transcript_264','EG_transcript_26410','EG_transcript_26412','EG_transcript_26449','EG_transcript_26455','EG_transcript_2646','EG_transcript_26477','EG_transcript_26585','EG_transcript_26638','EG_transcript_26675','EG_transcript_26742','EG_transcript_26745','EG_transcript_26750','EG_transcript_26805','EG_transcript_26871','EG_transcript_2696','EG_transcript_26973','EG_transcript_2698','EG_transcript_27050','EG_transcript_27059','EG_transcript_27105','EG_transcript_27131','EG_transcript_27210','EG_transcript_27254','EG_transcript_27273','EG_transcript_2731','EG_transcript_27347','EG_transcript_27366','EG_transcript_2741','EG_transcript_27500','EG_transcript_27516','EG_transcript_276','EG_transcript_27641','EG_transcript_27692','EG_transcript_27705','EG_transcript_27716','EG_transcript_27781','EG_transcript_27932','EG_transcript_27970','EG_transcript_2824','EG_transcript_28279','EG_transcript_28375','EG_transcript_2839','EG_transcript_2843','EG_transcript_28557','EG_transcript_28653','EG_transcript_28690','EG_transcript_28774','EG_transcript_2883','EG_transcript_28843','EG_transcript_28934','EG_transcript_2898','EG_transcript_28989','EG_transcript_29064','EG_transcript_29168','EG_transcript_29203','EG_transcript_29249','EG_transcript_2935','EG_transcript_29409','EG_transcript_29479','EG_transcript_2948','EG_transcript_2950','EG_transcript_29541','EG_transcript_29558','EG_transcript_29565','EG_transcript_2957','EG_transcript_29641','EG_transcript_2965','EG_transcript_2979','EG_transcript_298','EG_transcript_29857','EG_transcript_29866','EG_transcript_29941','EG_transcript_29972','EG_transcript_30136','EG_transcript_30159','EG_transcript_30166','EG_transcript_30359','EG_transcript_3042','EG_transcript_30512','EG_transcript_30526','EG_transcript_30576','EG_transcript_3060','EG_transcript_30657','EG_transcript_30668','EG_transcript_30675','EG_transcript_3075','EG_transcript_30775','EG_transcript_30862','EG_transcript_31056','EG_transcript_31130','EG_transcript_3116','EG_transcript_31285','EG_transcript_31334','EG_transcript_31367','EG_transcript_31449','EG_transcript_31497','EG_transcript_31652','EG_transcript_3168','EG_transcript_31803','EG_transcript_31942','EG_transcript_3196','EG_transcript_32001','EG_transcript_32019','EG_transcript_32046','EG_transcript_32139','EG_transcript_3221','EG_transcript_32263','EG_transcript_32322','EG_transcript_32395','EG_transcript_32401','EG_transcript_3246','EG_transcript_32547','EG_transcript_3260','EG_transcript_32677','EG_transcript_3272','EG_transcript_3275','EG_transcript_32842','EG_transcript_32904','EG_transcript_32956','EG_transcript_33117','EG_transcript_33134','EG_transcript_33180','EG_transcript_33208','EG_transcript_33225','EG_transcript_33278','EG_transcript_33313','EG_transcript_33323','EG_transcript_33336','EG_transcript_33398','EG_transcript_3342','EG_transcript_33577','EG_transcript_33627','EG_transcript_3363','EG_transcript_3371','EG_transcript_33830','EG_transcript_3387','EG_transcript_33930','EG_transcript_3395','EG_transcript_3397','EG_transcript_3398','EG_transcript_34043','EG_transcript_34143','EG_transcript_34241','EG_transcript_3451','EG_transcript_3460','EG_transcript_34605','EG_transcript_3471','EG_transcript_3480','EG_transcript_35144','EG_transcript_3515','EG_transcript_35155','EG_transcript_35367','EG_transcript_3547','EG_transcript_35473','EG_transcript_35487','EG_transcript_35652','EG_transcript_35745','EG_transcript_35814','EG_transcript_35867','EG_transcript_36013','EG_transcript_36015','EG_transcript_36079','EG_transcript_36144','EG_transcript_36233','EG_transcript_36254','EG_transcript_3632','EG_transcript_3639','EG_transcript_36591','EG_transcript_3663','EG_transcript_36680','EG_transcript_36734','EG_transcript_37041','EG_transcript_37233','EG_transcript_37274','EG_transcript_37320','EG_transcript_37345','EG_transcript_37499','EG_transcript_37569','EG_transcript_37612','EG_transcript_3774','EG_transcript_3780','EG_transcript_37917','EG_transcript_37938','EG_transcript_37971','EG_transcript_38444','EG_transcript_38479','EG_transcript_3851','EG_transcript_38569','EG_transcript_38657','EG_transcript_3873','EG_transcript_38786','EG_transcript_3882','EG_transcript_38875','EG_transcript_3895','EG_transcript_3898','EG_transcript_39302','EG_transcript_3952','EG_transcript_39546','EG_transcript_39671','EG_transcript_39815','EG_transcript_39893','EG_transcript_39982','EG_transcript_3999','EG_transcript_4006','EG_transcript_40131','EG_transcript_40187','EG_transcript_4021','EG_transcript_40410','EG_transcript_40417','EG_transcript_40456','EG_transcript_40617','EG_transcript_40903','EG_transcript_40935','EG_transcript_41067','EG_transcript_4109','EG_transcript_4115','EG_transcript_41155','EG_transcript_41443','EG_transcript_4145','EG_transcript_41526','EG_transcript_41706','EG_transcript_4177','EG_transcript_41871','EG_transcript_4204','EG_transcript_42050','EG_transcript_4221','EG_transcript_42708','EG_transcript_42871','EG_transcript_4296','EG_transcript_43','EG_transcript_43106','EG_transcript_43339','EG_transcript_4343','EG_transcript_43430','EG_transcript_4344','EG_transcript_4365','EG_transcript_4373','EG_transcript_43781','EG_transcript_43895','EG_transcript_4413','EG_transcript_4427','EG_transcript_443','EG_transcript_44308','EG_transcript_44414','EG_transcript_4466','EG_transcript_4487','EG_transcript_4496','EG_transcript_45445','EG_transcript_4546','EG_transcript_45528','EG_transcript_45706','EG_transcript_45748','EG_transcript_46063','EG_transcript_4631','EG_transcript_4662','EG_transcript_4666','EG_transcript_46758','EG_transcript_4676','EG_transcript_4696','EG_transcript_47045','EG_transcript_47055','EG_transcript_4713','EG_transcript_4714','EG_transcript_47196','EG_transcript_4731','EG_transcript_4738','EG_transcript_4741','EG_transcript_4759','EG_transcript_47615','EG_transcript_4764','EG_transcript_47790','EG_transcript_47923','EG_transcript_4839','EG_transcript_48427','EG_transcript_487','EG_transcript_48747','EG_transcript_48888','EG_transcript_49040','EG_transcript_4905','EG_transcript_4918','EG_transcript_49195','EG_transcript_49250','EG_transcript_4934','EG_transcript_49389','EG_transcript_4939','EG_transcript_4951','EG_transcript_49741','EG_transcript_4976','EG_transcript_49834','EG_transcript_5','EG_transcript_50152','EG_transcript_50185','EG_transcript_5021','EG_transcript_50555','EG_transcript_50680','EG_transcript_5076','EG_transcript_50903','EG_transcript_5140','EG_transcript_5154','EG_transcript_5157','EG_transcript_5202','EG_transcript_52197','EG_transcript_52320','EG_transcript_5257','EG_transcript_5258','EG_transcript_53084','EG_transcript_5315','EG_transcript_5340','EG_transcript_53540','EG_transcript_5356','EG_transcript_53971','EG_transcript_5418','EG_transcript_54211','EG_transcript_5426','EG_transcript_5443','EG_transcript_5444','EG_transcript_54525','EG_transcript_5458','EG_transcript_54753','EG_transcript_5488','EG_transcript_5572','EG_transcript_5575','EG_transcript_55768','EG_transcript_5580','EG_transcript_5584','EG_transcript_56112','EG_transcript_56241','EG_transcript_5628','EG_transcript_5645','EG_transcript_5646','EG_transcript_56699','EG_transcript_5683','EG_transcript_56921','EG_transcript_573','EG_transcript_57369','EG_transcript_5750','EG_transcript_5767','EG_transcript_5780','EG_transcript_5801','EG_transcript_5832','EG_transcript_5838','EG_transcript_5843','EG_transcript_58635','EG_transcript_58857','EG_transcript_58911','EG_transcript_5903','EG_transcript_59112','EG_transcript_59212','EG_transcript_5925','EG_transcript_5934','EG_transcript_59393','EG_transcript_5944','EG_transcript_59561','EG_transcript_59663','EG_transcript_59776','EG_transcript_5997','EG_transcript_60044','EG_transcript_6007','EG_transcript_6024','EG_transcript_60280','EG_transcript_60294','EG_transcript_6030','EG_transcript_60352','EG_transcript_6045','EG_transcript_6076','EG_transcript_61133','EG_transcript_61190','EG_transcript_61600','EG_transcript_61761','EG_transcript_62166','EG_transcript_6250','EG_transcript_6252','EG_transcript_6253','EG_transcript_6257','EG_transcript_6269','EG_transcript_628','EG_transcript_6291','EG_transcript_63','EG_transcript_63059','EG_transcript_6306','EG_transcript_6313','EG_transcript_6315','EG_transcript_63243','EG_transcript_64','EG_transcript_6401','EG_transcript_64535','EG_transcript_64542','EG_transcript_64640','EG_transcript_6467','EG_transcript_64724','EG_transcript_6473','EG_transcript_64754','EG_transcript_64916','EG_transcript_65','EG_transcript_6510','EG_transcript_65902','EG_transcript_6595','EG_transcript_6602','EG_transcript_6618','EG_transcript_6624','EG_transcript_6656','EG_transcript_66661','EG_transcript_67616','EG_transcript_6763','EG_transcript_68092','EG_transcript_6835','EG_transcript_68504','EG_transcript_6865','EG_transcript_6878','EG_transcript_68843','EG_transcript_6918','EG_transcript_6932','EG_transcript_6933','EG_transcript_6941','EG_transcript_6982','EG_transcript_69851','EG_transcript_7051','EG_transcript_70750','EG_transcript_70755','EG_transcript_7076','EG_transcript_70801','EG_transcript_7094','EG_transcript_71144','EG_transcript_7126','EG_transcript_7147','EG_transcript_715','EG_transcript_71593','EG_transcript_7177','EG_transcript_7178','EG_transcript_72058','EG_transcript_724','EG_transcript_7299','EG_transcript_7331','EG_transcript_7357','EG_transcript_7411','EG_transcript_7450','EG_transcript_7523','EG_transcript_7532','EG_transcript_7534','EG_transcript_7558','EG_transcript_7567','EG_transcript_7573','EG_transcript_7594','EG_transcript_760','EG_transcript_7601','EG_transcript_7616','EG_transcript_7650','EG_transcript_7732','EG_transcript_7761','EG_transcript_7775','EG_transcript_7782','EG_transcript_7788','EG_transcript_7801','EG_transcript_7808','EG_transcript_7817','EG_transcript_7818','EG_transcript_7857','EG_transcript_7877','EG_transcript_7879','EG_transcript_7896','EG_transcript_790','EG_transcript_791','EG_transcript_7940','EG_transcript_7963','EG_transcript_7967','EG_transcript_8006','EG_transcript_8016','EG_transcript_8021','EG_transcript_8090','EG_transcript_8095','EG_transcript_8117','EG_transcript_8143','EG_transcript_8156','EG_transcript_8168','EG_transcript_8174','EG_transcript_822','EG_transcript_8223','EG_transcript_8289','EG_transcript_8297','EG_transcript_8323','EG_transcript_8364','EG_transcript_8383','EG_transcript_8430','EG_transcript_8456','EG_transcript_8464','EG_transcript_8471','EG_transcript_8502','EG_transcript_8525','EG_transcript_8528','EG_transcript_8546','EG_transcript_8552','EG_transcript_8585','EG_transcript_8615','EG_transcript_862','EG_transcript_8645','EG_transcript_8651','EG_transcript_8679','EG_transcript_8688','EG_transcript_8750','EG_transcript_8779','EG_transcript_8825','EG_transcript_8836','EG_transcript_8875','EG_transcript_891','EG_transcript_8912','EG_transcript_8914','EG_transcript_8975','EG_transcript_8993','EG_transcript_9','EG_transcript_9017','EG_transcript_9051','EG_transcript_9052','EG_transcript_9064','EG_transcript_9071','EG_transcript_9097','EG_transcript_9103','EG_transcript_9150','EG_transcript_9181','EG_transcript_9184','EG_transcript_9247','EG_transcript_9270','EG_transcript_9324','EG_transcript_9328','EG_transcript_9333','EG_transcript_9338','EG_transcript_9396','EG_transcript_9425','EG_transcript_9431','EG_transcript_9443','EG_transcript_9466','EG_transcript_9513','EG_transcript_9522','EG_transcript_9571','EG_transcript_9615','EG_transcript_9616','EG_transcript_9632','EG_transcript_9640','EG_transcript_9658','EG_transcript_9664','EG_transcript_9682','EG_transcript_9695','EG_transcript_97','EG_transcript_971','EG_transcript_9716','EG_transcript_9736','EG_transcript_9746','EG_transcript_975','EG_transcript_9824','EG_transcript_9827','EG_transcript_9836','EG_transcript_9849','EG_transcript_985','EG_transcript_9855','EG_transcript_9858','EG_transcript_9899','EG_transcript_9915','EG_transcript_9941','EG_transcript_9967','EG_transcript_9987']
f = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/data/euglena_all_proteins.fasta'
results = []

for record in SeqIO.parse(f, "fasta"):
    if record.id in mitolist:
        results.append(record)

outpath = '/home/anna/Dropbox/phd/mitoproteomes/proteomes/euglena/data/euglena_final_mito_proteins.fasta'

SeqIO.write(results, outpath, "fasta")