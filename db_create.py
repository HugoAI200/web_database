from config import db
from models import Metadata, Identification, content_Information, Distribution, DataQuality, ReferenceSystem,\
                   portrayalCatalogueReference, ApplicationScheInformaton, Constraints, MaintenanceInformation,\
                   Keyword, BrowseGraphic, AgrregateInformation, TopicCategory,DigitalTransferOptions, ditributor,\
                   Format, Medium, Lineage

from models import EQAdditionalInformation, Extent, GeographicExtent, TemporalExtent, VerticalExtent, Citation, Contact_Phone,\
                   Address, Date, OnLineResource, Series, Telephone


db.create_all()
# Define02 = Metadata("元数据的唯一标识符", "元数据使用的语言", "元数据集使用的字符编码标准的全名", "对元数据信息负责的单位或个人",
#                     "元数据创建的日期", "执行的元数据标准名称", "执行的元数据标准版本", "元数据描述的资源的基本信息",
#                     "数据内容特征的描述信息", "获取资源所需的分发者和分发方式的信息", "资源质量的总体评价信息", "数据集采用的空间和时间参照系说明",
#                     "资源图示表达而规定的编目规则信息", "数据集概念模式的信息", "访问和使用元数据的限制信息", "元数据的更新频率及更新范围的信息",)
# Define03 = Identification("与数据集有关的基本信息","资源内容的简单说明","资源开发的目的说明","对资源做出贡献者的认可","资源的状况",
#                                      "与资源有关的人或单位，及与其通讯的方法","数据集更新频率和更新范围的信息","概要性说明资源（应包括图例）的图形",
#                                      "数据集的格式说明","关键字种类、类型和参考资料","数据集的限制信息", "与本数据集相关的数据集系列的信息",
#                                      "在空间上表示地理信息所使用的方法", "一般了解数据集中空间数据密度的参数", "用硬拷贝地图或海图的比例尺表示的详细程度",
#                                      "地面采样间隔","标识卫星影像数据集或卫星影像数据集系列所需要的信息","地理信息单元标识符", "获取影像数据所使用的卫星",
#                                      "观测仪器[传感器名称","单景影像的时间标识","影像覆盖的列和行标识","影像覆盖的轨道个数", "数据集采用的语言",
#                                      "数据集使用的字符编码标准全称", "数据集的分类信息","覆盖范围信息包括数据集边界多边形、垂直方向范围和时间范围等",
#                                      "提供关于地震数据的附加属性")
# Define04 = BrowseGraphic("包含数据集图解说明的图形文件名称", "数据集图解的文件说明", "图解图形编码格式，如CGM、EPS、GIF、JPEG、PBM、PS、TIFF、XWD")
# Define05 = Keyword("用于描述主题的通用词、形式化词或短语，数据的质量信息", "正式注册的词典或类似的权威关键词资料的基本信息")
# Define06 = AgrregateInformation("相关数据集的基本信息", "相关数据集的关联信息", "产生相关数据集的初始类型")
# Define07 = TopicCategory("用于描述数据集类别的通用词、形式化词或短语", "类别名称对应的编码", "分类标准名称")
# Define08 = content_Information("数据集所在的资源范围", "数据集内容描述", "有关网格数据网格单元内容的信息",
#                                "用度量值表示的属性说明","用网格单元值表示的信息类型")
# Define09 = Distribution("格式说明", "分发者的信息", "从分发者获取资料的技术方法和介质")
# Define10 = DigitalTransferOptions("可以使用数据的名称、数据层、地理范围等", "按确定的传送格式估计，一个分发单元的传送量，用MB表示。传送量〉0.0",
#                                   "可以获取资源的在线资源信息", "可以获取资源的离线介质信息")
# Define11 = ditributor("可以获取资源的单位。不要求单位列表是穷举的")
# Define12 = Format("数据传送格式名称", "格式版本（日期、版本号等）","格式版本的修订号","格式的子集、专用标准或产品规范名称",
#                   "能够用来读取资源，或对经过压缩的资源进行解压的算法或处理说明")
# Define13 = Medium("能够接收资源的介质名称")
# Define14 = DataQuality("数据质量范围内，数据的质量信息")
# Define15 = Lineage("数据生产者有关数据集数据志信息的一般说明")
# Define16 = ReferenceSystem("坐标系统的元数据", "所用投影的名称", "所用椭球体的名称", "所用基准的标识",
#                                               "数据集使用的时间参照系说明", "使用的时间参照系名称", "所用时间基准的标识")
# Define17 = portrayalCatalogueReference("图示表达目录引用的参考文献目录")
# Define18 = ApplicationScheInformaton("使用的应用模式名称", "使用的模式语言标识", "应用模式使用的形式语言", "用ASCII文件给出的完整应用模式",
#                                               "用图形文件给出的完整应用模式", "用软件开发文件给出的完整应用模式", "用于应用模式软件相关文件的软件相关格式")
# Define19 = Constraints("影响资源或元数据适用性的限制，如“不可用于导航”", "访问和使用资源或元数据的限制和法律上的先决条件"
#                                    , "为确保隐私权或保护知识产权，对获取资源或元数据施加的访问限制，以及任何特殊的约束或限制"
#                                    ,"为确保隐私安全或保护知识产权，对使用资源或元数据施加的使用限制，以及任何特殊的约束、限制或声明",
#                                    "为了国家安全或类似的安全考虑，对资源或元数据施加的处理限制", "对资源或元数据处理限制的名称")
# Define20 = MaintenanceInformation("在资源初次完成后，对其进行修改和补充的频率", "联系负责人维护元数据的人和单位的标识和方法")
# ## Define01.MaintInfo_1.append(MaintenanceInformation("one year", "金震"))
# ## Define02.MaintInfo_2.append(MaintenanceInformation("one year", "金震"))
#
# Define21 = EQAdditionalInformation("地震数据集的获取途径", "对于地震观测数据的描述", "台站基础数据文件名", "台网基础数据文件名", "采样率",
#                                    "探测手段描述", "测线/台阵覆盖范围",
#                                    "探测时段", "调查数据描述", "调查方法/手段", "调查报告文件名",
#                                    "是否是大地震发生现场", "地震参数", "调查时段",
#                                    "调查范围", "实验数据描述", "地震实验室类别", "地震实验室资质",
#                                    "实验报告文件名", "专项数据", "项目名称", "项目来源", "项目执行时段",
#                                    "项目概述", "数据库类别", "数据库级别")
# Define22 = Extent("有关对象的空间和时间覆盖范围", "有关对象覆盖范围的地理组成部分", "有关对象覆盖范围的时间组成部分", "台有关对象覆盖范围的垂向组成部分")
# Define23 = GeographicExtent("数据集的地理位置。注意：这仅仅是近似的范围，无需说明坐标系统", "数据集覆盖范围最西边坐标，用十进制经度表示（东半球为正）",
#                             "数据集覆盖范围最东边坐标，用十进制经度表示（东半球为正）", "数据集覆盖范围最南边坐标，用十进制纬度表示（北半球为正）",
#                             "数据集覆盖范围最北边坐标，用十进制纬度表示（北半球为正）", "用作标识符的地理区域说明", "用于说明地理区域的标识符")
# Define24 = TemporalExtent("数据集内容的日期和时间", "数据集原始数据生成或采集跨越的时间段", "数据集原始数据生成或采集的起始时间", "数据集原始数据生成或采集的终止时间")
# Define25 = VerticalExtent("数据集包含的垂向范围最低值", "数据集包含的垂向范围最高值", "用于垂向范围信息的度量单位。例如：米、英尺、厘米、百帕", "度量垂向范围覆盖范围最大值和最小值的原点信息")
# Define26 = Citation("已知的引用资源名称", "已知引用信息的短名或用其它语言表述的名称", "引用资源的有关日期", "引用资源的版本", "出版日期",
#                                    "对引用资源负责的人或单位的名称和地址信息", "引用资源的表达方式",
#                                    "数据集为其一部分的数据集系列或聚集数据集信息", "完成对其它地方未记录的资源引用所需的其它信息", "带注释的公共名称",
#                                    "国际标准书号", "国际标准系列号", "有关的负责者和单位的标识及联系方法",
#                                    "负责者姓、名、头衔，用分隔符隔开", "负责单位名", "负责者角色或职务",
#                                    "负责单位地址", "负责方所履行的职责")
# Define27 = Address("位置的详细地址", "所在城市", "所在省、自治区、直辖市", "所在城市" , "邮政编码" , "所在国家"
#                    "负责者或负责单位邮件地址")
# Define28 = Contact_Phone("可以与负责人或负责单位联系的电话号码", "可以与负责人或负责单位联系的物理地址和电子邮件地址", "可以用于与负责人或负责单位联系的在线信息",
#                    "可以与负责人或负责单位联系的时间段（包括时区" ,"如何或何时与负责人或负责单位联系的补充说明")
# Define29 = Date("引用资源的参照日期", "使用该日期的事件")
# Define30 = OnLineResource("使用URL地址与类似地址模式，如http://www.statkart.no/isotc211/，进行在线访问的地址",
#                           "使用的连接协议", "可以与在线资源一起使用的专用领域专用标准名",
#                    "在线资源名称" ,"在线资源是什么/做什么的详细文字说明","在线资源功能代码")
# Define31 = Series("数据集为其一部分的数据集系列或聚集数据集名称",
#                    "系列的版本标识信息" ,"刊登有关内容的出版物页码的详细说明")
# Define32 = Telephone("能与负责人或负责单位通话的电话号码",
#                    "负责人或负责单位的传真号码")

# db.session.add(Define02)
# db.session.add(Define03)
# db.session.add(Define04)
# db.session.add(Define05)
# db.session.add(Define06)
# db.session.add(Define07)
# db.session.add(Define08)
# db.session.add(Define09)
# db.session.add(Define10)
# db.session.add(Define11)
# db.session.add(Define12)
# db.session.add(Define13)
# db.session.add(Define14)
# db.session.add(Define15)
# db.session.add(Define16)
# db.session.add(Define17)
# db.session.add(Define18)
# db.session.add(Define19)
# db.session.add(Define20)
# db.session.add(Define21)
# db.session.add(Define22)
# db.session.add(Define23)
# db.session.add(Define24)
# db.session.add(Define25)
# db.session.add(Define26)
# db.session.add(Define27)
# db.session.add(Define28)
# db.session.add(Define29)
# db.session.add(Define30)
# db.session.add(Define31)
# db.session.add(Define32)
########                  增加
##############################################################
Add_query = EQAdditionalInformation("2018年obs数据集", "segy格式", "30202", "福建OBS流动台网", "250",
                                   "可移动式大容量气枪", "N：21-28 E：115-122",
                                   "探测时段", "调查数据描述", "调查方法/手段", "调查报告文件名",
                                   "是否是大地震发生现场", "地震参数", "调查时段",
                                   "调查范围", "实验数据描述", "地震实验室类别", "地震实验室资质",
                                   "实验报告文件名", "专项数据", "项目名称", "项目来源", "项目执行时段",
                                   "项目概述", "数据库类别", "数据库级别")
db.session.add(Add_query)
##############################################################
########                  删除
##############################################################
# Delete_query = db.session.query(EQAdditionalInformation).filter_by(id='2').first()
# db.session.delete(Delete_query)
##############################################################
########                  更新
##############################################################
# Update_query = db.session.query(Date).filter_by(id='2').first()
# Update_query.refDate = "优秀"
##############################################################
########                  查询
##############################################################
# Read_query = db.session.query(Date).filter_by(id='2').first()
# print('type:{0}'.format(type(Read_query)))
# print('name:{0}'.format(Read_query.refDate))
##############################################################
db.session.commit()
db.session.close()
