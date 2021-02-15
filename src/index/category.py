# 目录管理
import src.server.res as res
from src.server import Server, req
from src.util import Singleton, ToolUtil, Log


class CateGoryBase(object):
    def __init__(self):
        self._id = ""            # 标识
        self.title = ""         # 标题
        self.description = ""          # 描述
        self.thumb = ""  # (fileServer, path, originalName)

    @property
    def id(self):
        return self._id


class CateGoryMgr(Singleton):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.idToCateGoryBase = []    # id: CateGoryBase

    @property
    def server(self):
        return Server()

    # 初始化目录
    def UpdateCateGory(self, bakParam=0):
        self.server.Send(req.CategoryReq(), bakParam=bakParam)

    def UpdateCateGoryBack(self, backData):
        for info in backData.res.data.get("categories", {}):
            if not info.get('_id'):
                continue
            newInfo = CateGoryBase()
            ToolUtil.ParseFromData(newInfo, info)
            self.idToCateGoryBase.append(newInfo)
        Log.Info("初始化目录成功。。。")
        return