from config import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref

class Metadata(db.Model):
    __tablename__ = "元数据"                      #   表：表02　元数据
    id = db.Column(db.Integer, primary_key=True)
    mdID = db.Column(db.String(512))
    mdLang = db.Column(db.String(512))
    mdChar= db.Column(db.String(512))
    mdContact = db.Column(db.String(512))
    mdDateSt = db.Column(db.String(512))
    mdStanName = db.Column(db.String(512))
    mdStanVer = db.Column(db.String(512))
    dataldInfo = db.Column(db.String(512))
    contInfo = db.Column(db.String(512))
    distInfo = db.Column(db.String(512))
    dqInfo = db.Column(db.String(512))
    refSysInfo = db.Column(db.String(512))
    porCatInfo = db.Column(db.String(512))
    dtSchInfo = db.Column(db.String(512))
    mdConst = db.Column(db.String(512))
    mdMaint = db.Column(db.String(512))
    #
    Ident_1 = relationship("Identification", backref="1")
    ContInfo_1 = relationship("content_Information", backref="1")
    Distrib_1 = relationship("Distribution", backref="1")
    DataQral_1 = relationship("DataQuality", backref="1")
    RefSystem_1 = relationship("ReferenceSystem", backref="1")
    PortCatRef_1 = relationship("portrayalCatalogueReference", backref="1")
    DtSchInfo_1 = relationship("ApplicationScheInformaton", backref="1")
    Consts_1 = relationship("Constraints", backref="1")
    MaintInfo_1 = relationship("MaintenanceInformation", backref="1")

    def __init__(self, mdID, mdLang, mdChar, mdContact, mdDateSt, mdStanName, mdStanVer,
                  dataldInfo, contInfo, distInfo, dqInfo, refSysInfo, porCatInfo, dtSchInfo, mdConst, mdMaint):
        self.mdID = mdID
        self.mdLang = mdLang
        self.mdChar = mdChar
        self.mdContact = mdContact
        self.mdDateSt = mdDateSt
        self.mdStanName = mdStanName
        self.mdStanVer = mdStanVer
        self.dataldInfo = dataldInfo
        self.contInfo = contInfo
        self.distInfo = distInfo
        self.dqInfo = dqInfo
        self.refSysInfo = refSysInfo
        self.porCatInfo = porCatInfo
        self.dtSchInfo = dtSchInfo
        self.mdConst = mdConst
        self.mdMaint = mdMaint

    def __repr__(self):
        return '<Metadata {}'.format(self.Metadata)

class Identification(db.Model):        #   表03：标识
    __tablename__ = '标识'
    id = db.Column(db.Integer, primary_key=True)
    idCitation = db.Column(db.String(512))
    idAbs = db.Column(db.String(512))
    idPurp = db.Column(db.String(512))
    idCredit = db.Column(db.String(512))
    idStatus = db.Column(db.String(512))
    idPoC = db.Column(db.String(512))
    resMaint = db.Column(db.String(512))
    graphOver = db.Column(db.String(512))
    dsFormat = db.Column(db.String(512))
    descKeyes = db.Column(db.String(512))
    resConst = db.Column(db.String(512))
    aggrInfo = db.Column(db.String(512))
    spatRpType = db.Column(db.String(512))
    DataScale = db.Column(db.String(512))
    equScale = db.Column(db.String(512))
    scaleDist = db.Column(db.String(512))
    ImageID = db.Column(db.String(512))
    granuleID = db.Column(db.String(512))
    Satelite = db.Column(db.String(512))
    Sensor = db.Column(db.String(512))
    PassSeqID = db.Column(db.String(512))
    agOrbID = db.Column(db.String(512))
    orbNum = db.Column(db.String(512))
    datalang = db.Column(db.String(512))
    dataChar = db.Column(db.String(512))
    tpCat = db.Column(db.String(512))
    dataExt = db.Column(db.String(512))
    eqAddInfo = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))
    MaintInfo_2 = relationship("MaintenanceInformation", backref="2")
    BrowGraph_2 = relationship("BrowseGraphic", backref="2")
    Format_2 = relationship("Format", backref="2")
    Keywords_2 = relationship("Keyword", backref="2")
    Consts_2 = relationship("Constraints", backref="2")
    AggregateInfo_2 = relationship("AgrregateInformation", backref="2")
    TpCat_2 = relationship("TopicCategory", backref="2")

    def __init__(self, idCitation, idAbs, idPurp, idCredit, idStatus, idPoC,resMaint,graphOver,dsFormat, descKeyes,resConst,aggrInfo,spatRpType
                 ,DataScale , equScale, scaleDist,ImageID ,granuleID ,Satelite,Sensor,PassSeqID,agOrbID,orbNum ,datalang,dataChar,tpCat ,dataExt,eqAddInfo):
        self.idCitation = idCitation
        self.idAbs = idAbs
        self.idPurp = idPurp
        self.idCredit = idCredit
        self.idStatus = idStatus
        self.idPoC = idPoC
        self.resMaint = resMaint
        self.graphOver = graphOver
        self.dsFormat = dsFormat
        self.descKeyes = descKeyes
        self.resConst = resConst
        self.aggrInfo = aggrInfo
        self.spatRpType = spatRpType
        self.DataScale = DataScale
        self.equScale = equScale
        self.scaleDist = scaleDist
        self.ImageID = ImageID
        self.granuleID = granuleID
        self.Satelite = Satelite
        self.Sensor = Sensor
        self.PassSeqID = PassSeqID
        self.agOrbID = agOrbID
        self.orbNum = orbNum
        self.datalang = datalang
        self.dataChar = dataChar
        self.tpCat= tpCat
        self.dataExt = dataExt
        self.eqAddInfo = eqAddInfo
    def __repr__(self):
        return '<idCitation {}'.format(self.idCitation)

class BrowseGraphic(db.Model):        #   表：表04　浏览图信息
    __tablename__ = '浏览图'
    id = db.Column(db.Integer, primary_key=True)
    bgFileName = db.Column(db.String(512))
    bgFileDesc = db.Column(db.String(512))
    bgfileType = db.Column(db.String(512))

    def __init__(self, bgFileName, bgFileDesc, bgfileType):
        self.bgFileName = bgFileName
        self.bgFileDesc = bgFileDesc
        self.bgfileType = bgfileType

    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __repr__(self):
        return '<idCitation {}'.format(self.bgFileName)

class Keyword(db.Model):        #   表：　表5　关键字信息
    __tablename__ = '关键字说明'
    id = db.Column(db.Integer, primary_key=True)
    keyword = db.Column(db.String(512))
    thesaInfo = db.Column(db.String(512))

    def __init__(self, keyword, thesaInfo):
        self.keyword = keyword
        self.thesaInfo = thesaInfo

    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __repr__(self):
        return '<idCitation {}'.format(self.keyword)

class AgrregateInformation(db.Model):        #   表：表6　相关数据集信息
    __tablename__ = '相关数据集信息'
    id = db.Column(db.Integer, primary_key=True)
    aggrDSInfo = db.Column(db.String(512))
    assocType = db.Column(db.String(512))
    initType = db.Column(db.String(512))

    def __init__(self, aggrDSInfo, assocType, initType):
        self.aggrDSInfo = aggrDSInfo
        self.assocType = assocType
        self.initType = initType

    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __repr__(self):
        return '<idCitation {}'.format(self.aggrDSInfo)

class TopicCategory(db.Model):        #   表：表7　数据集分类信息
    __tablename__ = '数据集分类信息'
    id = db.Column(db.Integer, primary_key=True)
    cateName = db.Column(db.String(512))
    cateCode = db.Column(db.String(512))
    cateStd = db.Column(db.String(512))

    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __init__(self, cateName, cateCode, cateStd):
        self.cateName = cateName
        self.cateCode = cateCode
        self.cateStd = cateStd

    def __repr__(self):
        return '<idCitation {}'.format(self.cateName)

class content_Information(db.Model):        #   表08：内容
    __tablename__ = '内容信息'
    id = db.Column(db.Integer, primary_key=True)
    resDomain = db.Column(db.String(512))
    contDesc = db.Column(db.String(512))
    CovDesc = db.Column(db.String(512))
    attDesc = db.Column(db.String(512))
    contentType = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))

    def __init__(self, resDomain, contDesc, CovDesc, attDesc, contentType):
        self.resDomain = resDomain
        self.contDesc = contDesc
        self.CovDesc = CovDesc
        self.attDesc = attDesc
        self.contentType = contentType

    def __repr__(self):
        return '<idCitation {}'.format(self.resDomain)

class Distribution(db.Model):  # 表09：分发
    __tablename__ = '分发信息'
    id = db.Column(db.Integer, primary_key=True)
    distFormat = db.Column(db.String(512))
    distributor = db.Column(db.String(512))
    distTranOp = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))

    def __init__(self, distFormat, distributor, distTranOp):
        self.distFormat = distFormat
        self.distributor = distributor
        self.distTranOp = distTranOp

    def __repr__(self):
        return '<idCitation {}'.format(self.distFormat)

class DigitalTransferOptions(db.Model):  # 表10　传送选项信息
    __tablename__ = '数字传送选项'
    id = db.Column(db.Integer, primary_key=True)
    unitsOfDist = db.Column(db.String(512))
    transSize = db.Column(db.String(512))
    onLineSrc = db.Column(db.String(512))
    offLineMed = db.Column(db.String(512))

    def __init__(self, unitsOfDist, transSize, onLineSrc, offLineMed):
        self.unitsOfDist = unitsOfDist
        self.transSize = transSize
        self.onLineSrc = onLineSrc
        self.offLineMed = offLineMed

    def __repr__(self):
        return '<idCitation {}'.format(self.unitsOfDist)

class ditributor(db.Model):        #  表11　分发者信息
    __tablename__ = '分发者'
    id = db.Column(db.Integer, primary_key=True)
    distorCont = db.Column(db.String(512))

    def __init__(self, distorCont):
        self.distorCont = distorCont

    def __repr__(self):
        return '<idCitation {}'.format(self.distorCont)

class Format(db.Model):  # 表12　格式信息
    __tablename__ = '格式信息'
    id = db.Column(db.Integer, primary_key=True)
    formatName = db.Column(db.String(512))
    formatVer = db.Column(db.String(512))
    formatAmdNum = db.Column(db.String(512))
    formatSpec = db.Column(db.String(512))
    fileDecmTech = db.Column(db.String(512))

    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __init__(self, formatName, formatVer, formatAmdNum, formatSpec, fileDecmTech):
        self.formatName = formatName
        self.formatVer = formatVer
        self.formatAmdNum = formatAmdNum
        self.formatSpec = formatSpec
        self.fileDecmTech = fileDecmTech


    def __repr__(self):
        return '<idCitation {}'.format(self.formatName)

class Medium(db.Model):        #   表13　介质信息
    __tablename__ = '介质信息'
    id = db.Column(db.Integer, primary_key=True)
    medName = db.Column(db.String(512))

    def __init__(self, medName):
        self.medName = medName

    def __repr__(self):
        return '<idCitation {}'.format(self.medName)

class DataQuality(db.Model):        #   表14：数据质量信息
    __tablename__ = '数据质量信息'
    id = db.Column(db.Integer, primary_key=True)
    dataLineage = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))

    def __init__(self, dataLineage):
        self.dataLineage = dataLineage

    def __repr__(self):
        return '<idCitation {}'.format(self.dataLineage)

class Lineage(db.Model):        #   表15　数据志信息
    __tablename__ = '数据志信息'
    id = db.Column(db.Integer, primary_key=True)
    statement = db.Column(db.String(512))

    def __init__(self, statement):
        self.statement = statement

    def __repr__(self):
        return '<idCitation {}'.format(self.statement)

class ReferenceSystem(db.Model):        #   表16：参照系
    __tablename__ = '参照系'
    id = db.Column(db.Integer, primary_key=True)
    CoRefSys = db.Column(db.String(512))
    projection = db.Column(db.String(512))
    ellipsoid = db.Column(db.String(512))
    datum = db.Column(db.String(512))
    TmRefSys = db.Column(db.String(512))
    tmRefSysName = db.Column(db.String(512))
    tmCode = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))

    def __init__(self, CoRefSys, projection, ellipsoid , datum , TmRefSys ,tmRefSysName, tmCode):
        self.CoRefSys = CoRefSys
        self.projection = projection
        self.ellipsoid = ellipsoid
        self.datum = datum
        self.TmRefSys = TmRefSys
        self.tmRefSysName = tmRefSysName
        self.tmCode = tmCode

    def __repr__(self):
        return '<idCitation {}'.format(self.CoRefSys)

class portrayalCatalogueReference(db.Model):        #   表17：图示表达目录信息
    __tablename__ = '图示表达目录基本信息'
    id = db.Column(db.Integer, primary_key=True)
    portCatCit = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))

    def __init__(self, portCatCit):
        self.portCatCit = portCatCit

    def __repr__(self):
        return '<idCitation {}'.format(self.portCatCit)

class ApplicationScheInformaton(db.Model):        #   表18：应用模式信息
    __tablename__ = '应用模式信息'
    id = db.Column(db.Integer, primary_key=True)
    asName = db.Column(db.String(512))
    asSchLang = db.Column(db.String(512))
    asCstaLang = db.Column(db.String(512))
    asAscii = db.Column(db.String(512))
    asGraFile = db.Column(db.String(512))
    asSwDevFile = db.Column(db.String(512))
    asSwDevFiFt = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))

    def __init__(self, asName, asSchLang, asCstaLang  , asAscii , asGraFile ,asSwDevFile, asSwDevFiFt):
        self.asName = asName
        self.asSchLang = asSchLang
        self.asCstaLang  = asCstaLang
        self.asAscii = asAscii
        self.asGraFile = asGraFile
        self.asSwDevFile = asSwDevFile
        self.asSwDevFiFt = asSwDevFiFt

    def __repr__(self):
        return '<idCitation {}'.format(self.asName)
class Constraints(db.Model):        #   表19：限制
    __tablename__ = '限制信息'
    id = db.Column(db.Integer, primary_key=True)
    useLimit = db.Column(db.String(512))
    LegConsts = db.Column(db.String(512))
    accessConsts = db.Column(db.String(512))
    useConsts = db.Column(db.String(512))
    SecConsts = db.Column(db.String(512))
    Class = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))
    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __init__(self, useLimit, LegConsts, accessConsts, useConsts , SecConsts, Class):
        self.useLimit = useLimit
        self.LegConsts = LegConsts
        self.accessConsts  = accessConsts
        self.useConsts = useConsts
        self.SecConsts = SecConsts
        self.Class = Class
    def __repr__(self):
        return '<idCitation {}'.format(self.useLimit)

class MaintenanceInformation(db.Model):        #   表：表20　维护信息
    __tablename__ = '维护信息'
    id = db.Column(db.Integer, primary_key=True)
    mainFreq = db.Column(db.String(512))
    maintCont = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))
    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))
    def __init__(self, mainFreq, maintCont):
        self.mainFreq = mainFreq
        self.maintCont = maintCont

    def __repr__(self):
        return '<idCitation {}'.format(self.mainFreq)

class EQAdditionalInformation(db.Model):        #   表21　地震数据附加属性
    __tablename__ = '地震数据附加属性'
    id = db.Column(db.Integer, primary_key=True)
    eqDataAcWay = db.Column(db.String(512))
    ObDataDesc = db.Column(db.String(512))
    staDataFile = db.Column(db.String(512))
    netDataFile = db.Column(db.String(512))
    sampRate = db.Column(db.String(512))
    PsDataDesc = db.Column(db.String(512))
    psMeansDesc = db.Column(db.String(512))
    arrayCover = db.Column(db.String(512))
    psPeriod = db.Column(db.String(512))
    SvDataDesc = db.Column(db.String(512))
    svMethod = db.Column(db.String(512))
    svRepFile = db.Column(db.String(512))
    EqFieldSv = db.Column(db.String(512))
    eqPara = db.Column(db.String(512))
    svPeriod = db.Column(db.String(512))
    svCover = db.Column(db.String(512))
    ExDataDesc = db.Column(db.String(512))
    labType = db.Column(db.String(512))
    labQuali = db.Column(db.String(512))
    epRepFile = db.Column(db.String(512))
    PjData = db.Column(db.String(512))
    pjName = db.Column(db.String(512))
    pjOrigin = db.Column(db.String(512))
    pjExPeriod = db.Column(db.String(512))
    pjSummary = db.Column(db.String(512))
    dbType = db.Column(db.String(512))
    dbGrade = db.Column(db.String(512))

    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __init__(self, eqDataAcWay, ObDataDesc, staDataFile, netDataFile, sampRate, PsDataDesc,psMeansDesc,arrayCover,psPeriod, SvDataDesc,svMethod,svRepFile,
                 EqFieldSv , eqPara, svPeriod ,svCover ,ExDataDesc,labType, labQuali,epRepFile, PjData, pjName,pjOrigin,pjSummary, dbType, dbGrade):
        self.eqDataAcWay = eqDataAcWay
        self.ObDataDesc = ObDataDesc
        self.staDataFile = staDataFile
        self.netDataFile = netDataFile
        self.sampRate = sampRate
        self.PsDataDesc = PsDataDesc
        self.psMeansDesc = psMeansDesc
        self.arrayCover = arrayCover
        self.psPeriod = psPeriod
        self.SvDataDesc = SvDataDesc
        self.svMethod = svMethod
        self.svRepFile = svRepFile
        self.EqFieldSv = EqFieldSv
        self.eqPara = eqPara
        self.svPeriod = svPeriod
        self.svCover = svCover
        self.ExDataDesc = ExDataDesc
        self.labType = labType
        self.labQuali = labQuali
        self.epRepFile = epRepFile
        self.PjData = PjData
        self.pjName = pjName
        self.pjOrigin = pjOrigin
        self.pjSummary = pjSummary
        self.dbType = dbType
        self.dbGrade = dbGrade

    def __repr__(self):
        return '<idCitation {}'.format(self.eqDataAcWay)

class Extent(db.Model):        #   表22　概述
    __tablename__ = '概述'
    id = db.Column(db.Integer, primary_key=True)
    exDesc = db.Column(db.String(512))
    geoEle = db.Column(db.String(512))
    tempEle = db.Column(db.String(512))
    vertEle = db.Column(db.String(512))

    GeoExtent_21 = relationship("GeographicExtent", backref="2")
    TempExtent_21 = relationship("TemporalExtent", backref="2")
    VertExtent_21 = relationship("VerticalExtent", backref="2")
    Table_2 = db.Column(db.Integer, ForeignKey('标识.id'))

    def __init__(self, exDesc, geoEle, tempEle, vertEle):
        self.exDesc = exDesc
        self.geoEle = geoEle
        self.tempEle = tempEle
        self.vertEle = vertEle

    def __repr__(self):
        return '<idCitation {}'.format(self.exDesc)

class GeographicExtent(db.Model):        #   表23　地理覆盖范围信息
    __tablename__ = '地理覆盖范围信息'
    id = db.Column(db.Integer, primary_key=True)
    GeoBndBox = db.Column(db.String(512))
    westBL = db.Column(db.String(512))
    eastBL = db.Column(db.String(512))
    southBL = db.Column(db.String(512))
    northBL = db.Column(db.String(512))
    GeoDesc = db.Column(db.String(512))
    geoId = db.Column(db.String(512))

    Table_1 = db.Column(db.Integer, ForeignKey('元数据.id'))
    Table_21 = db.Column(db.Integer, ForeignKey('概述.id'))

    def __init__(self, GeoBndBox, westBL, eastBL, southBL , northBL ,GeoDesc, geoId ):
        self.GeoBndBox = GeoBndBox
        self.westBL = westBL
        self.eastBL = eastBL
        self.southBL = southBL
        self.northBL = northBL
        self.GeoDesc = GeoDesc
        self.geoId = geoId
    def __repr__(self):
        return '<idCitation {}'.format(self.GeoBndBox)

class TemporalExtent(db.Model):        #   表24　时间覆盖范围信息
    __tablename__ = '时间覆盖范围信息'
    id = db.Column(db.Integer, primary_key=True)
    exTemp = db.Column(db.String(512))
    Period = db.Column(db.String(512))
    begin = db.Column(db.String(512))
    end = db.Column(db.String(512))

    Table_21 = db.Column(db.Integer, ForeignKey('概述.id'))

    def __init__(self, exTemp, Period, begin, end):
        self.exTemp = exTemp
        self.Period = Period
        self.begin = begin
        self.end = end


    def __repr__(self):
        return '<idCitation {}'.format(self.exTemp)

class VerticalExtent(db.Model):        #   表25　垂向覆盖范围信息
    __tablename__ = '垂向覆盖范围信息'
    id = db.Column(db.Integer, primary_key=True)
    vertMinVal = db.Column(db.String(512))
    vertMaxVal = db.Column(db.String(512))
    vertUoM = db.Column(db.String(512))
    vertDatum = db.Column(db.String(512))

    Table_21 = db.Column(db.Integer, ForeignKey('概述.id'))

    def __init__(self, vertMinVal, vertMaxVal ,vertUoM ,vertDatum ):
        self.vertMinVal = vertMinVal
        self.vertMaxVal = vertMaxVal
        self.vertUoM = vertUoM
        self.vertDatum = vertDatum


    def __repr__(self):
        return '<idCitation {}'.format(self.vertMinVal)

class Citation(db.Model):        #   表26　引用信息
    __tablename__ = '引用信息'
    id = db.Column(db.Integer, primary_key=True)
    resTitle = db.Column(db.String(512))
    resAltTitle = db.Column(db.String(512))
    resRefDate = db.Column(db.String(512))
    resEd = db.Column(db.String(512))
    resEdDate = db.Column(db.String(512))
    citRespParty = db.Column(db.String(512))
    presForm = db.Column(db.String(512))
    datasetSeries = db.Column(db.String(512))
    otherCitDet = db.Column(db.String(512))
    collTitle = db.Column(db.String(512))
    isbn = db.Column(db.String(512))
    issn = db.Column(db.String(512))
    respParty = db.Column(db.String(512))
    rpIndName = db.Column(db.String(512))
    rpOrgName = db.Column(db.String(512))
    rpPosName = db.Column(db.String(512))
    rpCntInfo = db.Column(db.String(512))
    role = db.Column(db.String(512))

    def __init__(self, resTitle , resAltTitle, resRefDate, resEd, resEdDate, citRespParty, spresForm, datasetSeries,otherCitDet,collTitle,isbn, issn,respParty,
                 rpIndName , rpOrgName, rpPosName ,rpCntInfo ,role):
        self.resTitle = resTitle
        self.resAltTitle = resAltTitle
        self.resRefDate = resRefDate
        self.resEd = resEd
        self.resEdDate = resEdDate
        self.citRespParty = citRespParty
        self.spresForm = spresForm
        self.datasetSeries = datasetSeries
        self.otherCitDet = otherCitDet
        self.collTitle = collTitle
        self.isbn = isbn
        self.issn = issn
        self.respParty = respParty
        self.rpIndName = rpIndName
        self.rpOrgName = rpOrgName
        self.rpPosName = rpPosName
        self.rpCntInfo = rpCntInfo
        self.Erole = role

    def __repr__(self):
        return '<idCitation {}'.format(self.resTitle)

class Address(db.Model):        #   表27　地址信息
    __tablename__ = '地址信息'
    id = db.Column(db.Integer, primary_key=True)
    delPoint = db.Column(db.String(512))
    city = db.Column(db.String(512))
    adminArea = db.Column(db.String(512))
    postCode = db.Column(db.String(512))
    country = db.Column(db.String(512))
    eMailAdd = db.Column(db.String(512))

    def __init__(self, delPoint, city ,adminArea ,postCode, country, eMailAdd):
        self.delPoint = delPoint
        self.city = city
        self.adminArea = adminArea
        self.postCode = postCode
        self.country = country
        self.eMailAdd = eMailAdd


    def __repr__(self):
        return '<idCitation {}'.format(self.delPoint)

class Contact_Phone(db.Model):        #   表28　联系信息
    __tablename__ = '联系信息'
    id = db.Column(db.Integer, primary_key=True)
    cntPhone = db.Column(db.String(512))
    cntAddress = db.Column(db.String(512))
    cntOnlineRes = db.Column(db.String(512))
    cntHours = db.Column(db.String(512))
    cntInstr = db.Column(db.String(512))

    def __init__(self, cntPhone, cntAddress, cntOnlineRes, cntHours, cntInstr):
        self.cntPhone = cntPhone
        self.cntAddress = cntAddress
        self.cntOnlineRes = cntOnlineRes
        self.cntHours = cntHours
        self.cntInstr = cntInstr

    def __repr__(self):
        return '<idCitation {}'.format(self.cntPhone)

class Date(db.Model):        #   表29　日期信息
    __tablename__ = '日期信息'
    id = db.Column(db.Integer, primary_key=True)
    refDate = db.Column(db.String(512))
    refDateType = db.Column(db.String(512))

    def __init__(self, refDate, refDateType):
        self.refDate = refDate
        self.refDateType = refDateType

    def __repr__(self):
        return '<idCitation {}'.format(self.refDate)

class OnLineResource(db.Model):        #   表30　在线资源信息
    __tablename__ = '在线资源信息'
    id = db.Column(db.Integer, primary_key=True)
    linkage = db.Column(db.String(512))
    protocol = db.Column(db.String(512))
    appProfile = db.Column(db.String(512))
    orName = db.Column(db.String(512))
    orDesc = db.Column(db.String(512))
    orFunct = db.Column(db.String(512))

    def __init__(self, linkage, protocol, appProfile, orName , orDesc, orFunct):
        self.linkage = linkage
        self.protocol = protocol
        self.appProfile = appProfile
        self.orName = orName
        self.orDesc =orDesc
        self.orFunct = orFunct

    def __repr__(self):
        return '<idCitation {}'.format(self.linkage)

class Series(db.Model):        #   表31　系列信息
    __tablename__ = '系列信息'
    id = db.Column(db.Integer, primary_key=True)
    seriesName = db.Column(db.String(512))
    issId = db.Column(db.String(512))
    artPage = db.Column(db.String(512))

    def __init__(self, seriesName, issId, artPage):
        self.seriesName = seriesName
        self.issId = issId
        self.artPage = artPage

    def __repr__(self):
        return '<idCitation {}'.format(self.seriesName)


class Telephone(db.Model):  # 表32　电话信息
    __tablename__ = '电话信息'
    id = db.Column(db.Integer, primary_key=True)
    voiceNum = db.Column(db.String(512))
    faxNum = db.Column(db.String(512))

    def __init__(self, voiceNum, faxNum):
        self.voiceNum = voiceNum
        self.faxNum = faxNum

    def __repr__(self):
        return '<idCitation {}'.format(self.voiceNum)
