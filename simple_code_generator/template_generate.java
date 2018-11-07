package com.tccloud.webserver.service;

import com.tccloud.webserver.model.User;

public interface UserService{

    /**
     * 持久化User对象
     * @param user 要持久化的User对象
     */
    void save(User user);

    /**
     * 从数据库中删除掉User对象
     * @param user 要删除的User对象副本
     */
    void delete(User user);

    /**
     * 从数据库中获取类似的User对象
     * @param user 要获取的User对象的副本
     * @return 从数据库中获取到的User对象
     */
    User get(User user);

    /**
     * 根据提供的信息更新指定{model_name}
     * @param user 要查询的{model_name}
     * @return 返回跟新前的对象
     */
    User update(User user);
}


