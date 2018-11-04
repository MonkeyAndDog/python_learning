
package com.tccloud.webserver.dao.impl;


import com.tccloud.webserver.dao.UserDao;
import com.tccloud.webserver.model.User;


import org.springframework.orm.hibernate5.HibernateTemplate;
import org.springframework.stereotype.Component;
import javax.annotation.Resource;
import java.util.List;


@Component("userDao")
public class UserDaoImpl implements UserDao{


    private HibernateTemplate hibernateTemplate;


    public void save(User user){
        hibernateTemplate.save(user);
    }

    public void delete(User user){


    }


    public User get(User user){
        return null;
    }


    public List<User> getUsers(){
        return null;
    }


    public HibernateTemplate getHibernateTemplate(){
        return hibernateTemplate;
    }


    @Resource
    public void setHibernateTemplate(HibernateTemplate hibernateTemplate){
        this.hibernateTemplate = hibernateTemplate;
    }
}

