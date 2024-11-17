/*
 Navicat MySQL Data Transfer

 Source Server         : 本机
 Source Server Type    : MySQL
 Source Server Version : 80032
 Source Host           : localhost:3306
 Source Schema         : mmpt_shop

 Target Server Type    : MySQL
 Target Server Version : 80032
 File Encoding         : 65001

 Date: 07/05/2023 02:16:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for mmpt_admin
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_admin`;
CREATE TABLE `mmpt_admin`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `password` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '密码',
  `authority` int NOT NULL DEFAULT 2 COMMENT '1-系统管理员 2-操作员 3-商家',
  `address` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '地址',
  `phone` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '手机号',
  `email` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '电子邮件',
  `nom` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '姓名',
  `create_time` int NOT NULL DEFAULT 0 COMMENT '加入时间',
  `status` int NOT NULL DEFAULT 1 COMMENT '状态',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 7 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_admin
-- ----------------------------
INSERT INTO `mmpt_admin` VALUES (1, 'admin', '21232f297a57a5a743894a0e4a801fc3', 1, '广东茂名市文明北路', '13800138000', 'admin@126.com', '', 1254540424, 0);
INSERT INTO `mmpt_admin` VALUES (2, 'zjy', '21232f297a57a5a743894a0e4a801fc3', 2, '广东省深圳市福田区', '18898362320', 'zjy532@qq.com', '测试3', 1514896731, 1);
INSERT INTO `mmpt_admin` VALUES (4, 'mmpt', '21232f297a57a5a743894a0e4a801fc3', 2, '茂名市电白区沙院镇海城路五路', '13500135000', 'mmpt@qq.com', '21', 452424524, 1);
INSERT INTO `mmpt_admin` VALUES (5, 'wangjinjia', '21232f297a57a5a743894a0e4a801fc3', 2, '茂名市电白区沙院镇海城路五路', '13500135000', 'wangjinjia@qq.com', '', 245245245, 1);
INSERT INTO `mmpt_admin` VALUES (6, 'admin2', '21232f297a57a5a743894a0e4a801fc3', 1, '', '15001500000', 'admin@qq.com', '', 0, 1);
INSERT INTO `mmpt_admin` VALUES (7, 'CY', 'e10adc3949ba59abbe56e057f20f883e', 1, '', '16607512918', '1871263099@qq.com', '', 1683396890, 1);

-- ----------------------------
-- Table structure for mmpt_attributes
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_attributes`;
CREATE TABLE `mmpt_attributes`  (
  `aid` int NOT NULL AUTO_INCREMENT,
  `aname` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '属性名',
  `a_def_val` varchar(40) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '默认值',
  `cid` int NULL DEFAULT 0 COMMENT '分类id',
  PRIMARY KEY (`aid`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 39 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_attributes
-- ----------------------------
INSERT INTO `mmpt_attributes` VALUES (36, '类别', '烟', 22);
INSERT INTO `mmpt_attributes` VALUES (9, '类别', '蛋糕', 31);
INSERT INTO `mmpt_attributes` VALUES (10, '保质期', '180天', 31);
INSERT INTO `mmpt_attributes` VALUES (11, '商品编号', '20180101', 31);
INSERT INTO `mmpt_attributes` VALUES (12, '类别', '饼干', 30);
INSERT INTO `mmpt_attributes` VALUES (13, '保质期', '180天', 30);
INSERT INTO `mmpt_attributes` VALUES (14, '商品编号', '20180102', 30);
INSERT INTO `mmpt_attributes` VALUES (15, '类别', '巧克力', 29);
INSERT INTO `mmpt_attributes` VALUES (16, '保质期', '180天', 29);
INSERT INTO `mmpt_attributes` VALUES (17, '商品编号', '20180103', 29);
INSERT INTO `mmpt_attributes` VALUES (18, '类别', '糖果', 28);
INSERT INTO `mmpt_attributes` VALUES (19, '保质期', '180天', 28);
INSERT INTO `mmpt_attributes` VALUES (20, '商品编号', '20180104', 28);
INSERT INTO `mmpt_attributes` VALUES (21, '类别', '果干', 27);
INSERT INTO `mmpt_attributes` VALUES (22, '保质期', '180天', 27);
INSERT INTO `mmpt_attributes` VALUES (23, '商品编号', '20180105', 27);
INSERT INTO `mmpt_attributes` VALUES (24, '类别', '肉干', 26);
INSERT INTO `mmpt_attributes` VALUES (25, '保质期', '180天', 26);
INSERT INTO `mmpt_attributes` VALUES (26, '商品编号', '20180106', 26);
INSERT INTO `mmpt_attributes` VALUES (27, '类别', '炒货', 25);
INSERT INTO `mmpt_attributes` VALUES (28, '保质期', '180天', 25);
INSERT INTO `mmpt_attributes` VALUES (29, '商品编号', '20180107', 25);
INSERT INTO `mmpt_attributes` VALUES (30, '类别', '休闲食品', 24);
INSERT INTO `mmpt_attributes` VALUES (31, '保质期', '180天', 24);
INSERT INTO `mmpt_attributes` VALUES (32, '商品编号', '20180108', 24);
INSERT INTO `mmpt_attributes` VALUES (33, '类别', '啤酒饮料', 23);
INSERT INTO `mmpt_attributes` VALUES (34, '保质期', '180天', 23);
INSERT INTO `mmpt_attributes` VALUES (35, '商品编号', '20180109', 23);
INSERT INTO `mmpt_attributes` VALUES (37, '保质期', '360天', 22);
INSERT INTO `mmpt_attributes` VALUES (38, '商品编号', '20180110', 22);

-- ----------------------------
-- Table structure for mmpt_close
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_close`;
CREATE TABLE `mmpt_close`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `i_id` varchar(6) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `title` varchar(10) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  `sum` int NULL DEFAULT 0,
  `i_price` double(10, 2) NULL DEFAULT 0.00,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 37 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_close
-- ----------------------------
INSERT INTO `mmpt_close` VALUES (30, '28', '多味拼慕斯水果布丁茶', 1, 69.00);
INSERT INTO `mmpt_close` VALUES (31, '29', '包邮 套装 精酿 B', 1, 39.00);
INSERT INTO `mmpt_close` VALUES (32, '29', '精酿 Brewdog', 2, 19.00);
INSERT INTO `mmpt_close` VALUES (33, '30', '重庆牛浪汉牛肉干烧烤', 1, 98.00);
INSERT INTO `mmpt_close` VALUES (34, '31', '包邮 套装 精酿 B', 8, 39.00);
INSERT INTO `mmpt_close` VALUES (35, '32', '曼菲巧克力源于经典传', 5, 39.00);
INSERT INTO `mmpt_close` VALUES (36, '33', '曼菲巧克力源于经典传', 1, 39.00);

-- ----------------------------
-- Table structure for mmpt_column
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_column`;
CREATE TABLE `mmpt_column`  (
  `cid` int NOT NULL AUTO_INCREMENT,
  `cname` varchar(18) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '',
  `pid` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`cid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 32 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_column
-- ----------------------------
INSERT INTO `mmpt_column` VALUES (22, '香烟', 0);
INSERT INTO `mmpt_column` VALUES (23, '啤酒', 0);
INSERT INTO `mmpt_column` VALUES (24, '休闲', 0);
INSERT INTO `mmpt_column` VALUES (25, '炒货', 0);
INSERT INTO `mmpt_column` VALUES (26, '肉干', 0);
INSERT INTO `mmpt_column` VALUES (27, '果干', 0);
INSERT INTO `mmpt_column` VALUES (28, '糖果', 0);
INSERT INTO `mmpt_column` VALUES (29, '巧克力', 0);
INSERT INTO `mmpt_column` VALUES (30, '饼干', 0);
INSERT INTO `mmpt_column` VALUES (31, '蛋糕', 0);

-- ----------------------------
-- Table structure for mmpt_commodity
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_commodity`;
CREATE TABLE `mmpt_commodity`  (
  `g_id` int NOT NULL AUTO_INCREMENT COMMENT '商品id',
  `title` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '商品标题',
  `price` double(5, 0) NULL DEFAULT 0 COMMENT '商品价格',
  `stock` int NULL DEFAULT 0 COMMENT '商品库存',
  `cid` int NULL DEFAULT 0 COMMENT '栏目id',
  `del` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `time` int NULL DEFAULT 0,
  `status` varchar(4) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `interpret` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `aid` int NULL DEFAULT NULL,
  PRIMARY KEY (`g_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 108 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_commodity
-- ----------------------------
INSERT INTO `mmpt_commodity` VALUES (79, '休闲水果', 88, 899, 24, '0', 1515506888, '0', '/images/20180109/4de0d3a97dc19fddde97c0421eb6f6b5.jpg', 5);
INSERT INTO `mmpt_commodity` VALUES (80, '撩妹神器粉色樱花果冻', 29, 2000, 28, '0', 1515511723, '0', '/images/20180109/b4f4487f425bd4d1c3726cb075229d38.jpg', 5);
INSERT INTO `mmpt_commodity` VALUES (81, 'BELGIAN TRUFFLES原味经典松露巧克力', 39, 2000, 29, '0', 1515511818, '0', '/images/20180109/11082123bac948807911c3b2709d1a9e.jpg', 5);
INSERT INTO `mmpt_commodity` VALUES (82, '夹心巧克力经典草莓巧克力', 39, 2000, 29, '0', 1515511869, '0', '/images/20180109/93926fee147baf10566e6b4ba41df091.jpg', 5);
INSERT INTO `mmpt_commodity` VALUES (83, '卜珂8口味经典松露巧克力', 21, 2000, 29, '0', 1515511918, '0', '/images/20180109/8fdd2c2951b6247f8b812f80ecaaaec5.jpg', 5);
INSERT INTO `mmpt_commodity` VALUES (84, '卜珂8口味速溶巧克力', 29, 1000, 29, '0', 1515511960, '0', '/images/20180109/23d8c9704de9aab1b4cfa4596fdedc56.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (85, '卜珂8口味臻萃松露巧克力', 39, 500, 29, '0', 1515512036, '0', '/images/20180109/8486b4c3440477fb64fce0a8c6eb64dd.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (86, '曼菲巧克力源于经典传承美味', 39, 600, 29, '0', 1515512079, '0', '/images/20180109/2a7587af48b7317850a3227a49f0a60e.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (87, '俄罗斯进口德芙无花果牛奶巧克力休闲零食限区满包邮', 39, 600, 29, '0', 1515512139, '0', '/images/20180109/1b3b3f9d485552774820465cedcee969.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (88, '奥利奥巧克力夹心饼干原味/巧克力/草莓散称500g 包邮', 9, 600, 30, '0', 1515512189, '0', '/images/20180109/e27cbc24f2dcffa606fa28142f2c0aab.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (89, '【咕噜网】小王子 董小姐复合型烤薯片 巴西烤肉味 非油炸 约', 9, 500, 24, '0', 1515512271, '0', '/images/20180109/0743ffc79a1bded2b21393989f870372.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (90, '精酿 Brewdog Kingpin 酿酒狗 国王 21世纪', 19, 500, 23, '0', 1515514820, '0', '/images/20180109/054814d6bde5c31378cd01df66a3a67d.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (91, '包邮 套装 精酿 Blue Moon Wheat Ale 蓝', 39, 500, 23, '0', 1515512367, '0', '/images/20180109/98d8ceb86309b7cef6cbb364681431f2.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (92, '西班牙进口啤酒 INEDIT DAMM 艾帝达姆啤酒 750', 69, 500, 23, '0', 1515512408, '0', '/images/20180109/1c25cccc213d0a0462ce834937169c08.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (93, '美国savanna蜂蜜香烤杂烩混合坚果仁休闲零食850g', 19, 300, 24, '0', 1515512456, '0', '/images/20180109/d4d572fef63543ba275378a5de53708a.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (94, '百草味旗舰店冰糖山楂草莓芒果榴莲百香果干杨梅桃干蔬果条水果干', 29, 600, 27, '0', 1515512510, '0', '/images/20180109/8f62aa893528c4f49705f38c7ed7dcb1.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (95, '三只松鼠旗舰店水果干组合零食大礼包送女友12袋1212g芒果', 69, 600, 27, '0', 1515512558, '0', '/images/20180109/a5a4163825b60c102e0a78eef36850d0.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (96, '无核白葡萄干280gX2袋装三只松鼠零食蜜饯果干新疆特产提子', 39, 600, 27, '0', 1515512605, '0', '/images/20180109/f692479a7cfba8a886ceb80508570e2a.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (97, '糖豆小子手指形饼干 巧克力味酱40g 马来西亚进口宝宝吮指形', 19, 3000, 30, '0', 1515512652, '0', '/images/20180109/ddd29f0f5e0e21612d747efa454631cb.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (98, '进口零食丽芝士纳宝帝Richeese芝士夹心威化饼干145g', 39, 500, 30, '0', 1515512692, '0', '/images/20180109/f97e8ba5560be82684c2c78e0092f7bd.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (99, '德国原装Knoppers牛奶榛子巧克力威化饼干 250g（1', 39, 500, 30, '0', 1515512741, '0', '/images/20180109/72b8b8b465eaf4c88d254f733f1a0a7f.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (100, '巧罗手工可可脂黑白夹心巧克力婚庆喜糖糖果6款可选', 29, 500, 28, '0', 1515512803, '0', '/images/20180109/3652322ff4c9ab85a79f09fe7c0de1bc.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (101, '多味拼慕斯水果布丁茶点杯子聚会派对芒果榴莲蓝草莓玫瑰栗子蛋糕', 69, 2000, 31, '0', 1515512861, '0', '/images/20180109/759d1b336c70c22ecbff9002bd6a1682.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (102, '全场混2斤包邮 正宗糖果 阿尔卑斯硬糖口味随机混合500克 ', 19, 500, 28, '0', 1515512933, '0', '/images/20180109/34be9599ef396fc2804b338f1c096dc2.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (103, '阿尔卑斯牛奶糖水果硬糖500g约130颗结婚喜糖果年货零食散', 29, 500, 28, '0', 1515512980, '0', '/images/20180109/5ba26650333ee5e58cd077859b6812cd.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (105, '蜀道香麻辣味猪肉脯100g*2袋香辣猪肉干片牛肉干休闲辣味零', 39, 500, 26, '0', 1515514967, '0', '/images/20180109/5d497d985be2ab9b3e1a591afd2f79ca.jpg', NULL);
INSERT INTO `mmpt_commodity` VALUES (107, '重庆牛浪汉牛肉干烧烤味250g厂家直销 四川特产真空包装 日', 98, 121, 26, '0', 1515515361, '0', '/images/20180110/c27aff92a4f33f0c7883b49c3da83279.jpg', NULL);

-- ----------------------------
-- Table structure for mmpt_commondity_attr
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_commondity_attr`;
CREATE TABLE `mmpt_commondity_attr`  (
  `gaid` int NOT NULL AUTO_INCREMENT COMMENT 'id',
  `g_id` int NULL DEFAULT 0 COMMENT '商品id',
  `aname` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0' COMMENT '属性id',
  `avalue` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '属性值',
  PRIMARY KEY (`gaid`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 162 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_commondity_attr
-- ----------------------------
INSERT INTO `mmpt_commondity_attr` VALUES (56, 79, '商品编号', '21213123');
INSERT INTO `mmpt_commondity_attr` VALUES (55, 79, '保质期', '2121');
INSERT INTO `mmpt_commondity_attr` VALUES (54, 79, '类别', '21');
INSERT INTO `mmpt_commondity_attr` VALUES (57, 80, '类别', '糖果');
INSERT INTO `mmpt_commondity_attr` VALUES (58, 80, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (59, 80, '商品编号', '');
INSERT INTO `mmpt_commondity_attr` VALUES (60, 81, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (61, 81, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (62, 81, '商品编号', '20180102');
INSERT INTO `mmpt_commondity_attr` VALUES (63, 82, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (64, 82, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (65, 82, '商品编号', '20180103');
INSERT INTO `mmpt_commondity_attr` VALUES (66, 83, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (67, 83, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (68, 83, '商品编号', '20180104');
INSERT INTO `mmpt_commondity_attr` VALUES (69, 84, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (70, 84, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (71, 84, '商品编号', '20180105');
INSERT INTO `mmpt_commondity_attr` VALUES (72, 85, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (73, 85, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (74, 85, '商品编号', '20180106');
INSERT INTO `mmpt_commondity_attr` VALUES (75, 86, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (76, 86, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (77, 86, '商品编号', '20180107');
INSERT INTO `mmpt_commondity_attr` VALUES (78, 87, '类别', '巧克力');
INSERT INTO `mmpt_commondity_attr` VALUES (79, 87, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (80, 87, '商品编号', '20180108');
INSERT INTO `mmpt_commondity_attr` VALUES (81, 88, '类别', '饼干');
INSERT INTO `mmpt_commondity_attr` VALUES (82, 88, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (83, 88, '商品编号', '20180109');
INSERT INTO `mmpt_commondity_attr` VALUES (139, 104, '保质期', '30天');
INSERT INTO `mmpt_commondity_attr` VALUES (138, 104, '类别', '肉干');
INSERT INTO `mmpt_commondity_attr` VALUES (137, 106, '商品编号', '1');
INSERT INTO `mmpt_commondity_attr` VALUES (136, 106, '保质期', '1');
INSERT INTO `mmpt_commondity_attr` VALUES (135, 106, '类别', '1');
INSERT INTO `mmpt_commondity_attr` VALUES (140, 104, '商品编号', '02927288');
INSERT INTO `mmpt_commondity_attr` VALUES (141, 108, '类别', '');
INSERT INTO `mmpt_commondity_attr` VALUES (142, 108, '保质期', '');
INSERT INTO `mmpt_commondity_attr` VALUES (143, 108, '商品编号', '');
INSERT INTO `mmpt_commondity_attr` VALUES (144, 109, '类别', '');
INSERT INTO `mmpt_commondity_attr` VALUES (145, 109, '保质期', '');
INSERT INTO `mmpt_commondity_attr` VALUES (146, 109, '商品编号', '');
INSERT INTO `mmpt_commondity_attr` VALUES (147, 110, '类别', '11111');
INSERT INTO `mmpt_commondity_attr` VALUES (148, 110, '保质期', '1111');
INSERT INTO `mmpt_commondity_attr` VALUES (149, 110, '商品编号', '1111');
INSERT INTO `mmpt_commondity_attr` VALUES (150, 111, '类别', '11');
INSERT INTO `mmpt_commondity_attr` VALUES (151, 111, '保质期', '1111');
INSERT INTO `mmpt_commondity_attr` VALUES (152, 111, '商品编号', '');
INSERT INTO `mmpt_commondity_attr` VALUES (153, 112, '类别', '美国进口');
INSERT INTO `mmpt_commondity_attr` VALUES (154, 112, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (155, 112, '商品编号', '123');
INSERT INTO `mmpt_commondity_attr` VALUES (156, 112, '类别', 'jinkou');
INSERT INTO `mmpt_commondity_attr` VALUES (157, 112, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (158, 112, '商品编号', '123');
INSERT INTO `mmpt_commondity_attr` VALUES (159, 114, '类别', '11111');
INSERT INTO `mmpt_commondity_attr` VALUES (160, 114, '保质期', '180天');
INSERT INTO `mmpt_commondity_attr` VALUES (161, 114, '商品编号', '1');

-- ----------------------------
-- Table structure for mmpt_indent
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_indent`;
CREATE TABLE `mmpt_indent`  (
  `i_id` int NOT NULL AUTO_INCREMENT,
  `rid` int NULL DEFAULT 0 COMMENT '用户ID',
  `time` int NULL DEFAULT 0 COMMENT '添加时间',
  `manage` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0' COMMENT '是否处理订单',
  `del` varchar(2) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '0',
  `uid` int NULL DEFAULT 0,
  `i_status` int NULL DEFAULT 1,
  `trading_status` int NULL DEFAULT 2 COMMENT '0-交易失败 1-交易完成 2-交易中 3-删除',
  PRIMARY KEY (`i_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 34 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_indent
-- ----------------------------
INSERT INTO `mmpt_indent` VALUES (28, 6, 1515555550, '1', '1', 18, 1, 3);
INSERT INTO `mmpt_indent` VALUES (29, 6, 1515555552, '1', '1', 18, 1, 1);
INSERT INTO `mmpt_indent` VALUES (30, 6, 1515555553, '1', '1', 18, 1, 2);
INSERT INTO `mmpt_indent` VALUES (31, 8, 1515555555, '1', '1', 19, 1, 3);
INSERT INTO `mmpt_indent` VALUES (32, 8, 1515556995, '0', '0', 19, 1, 3);
INSERT INTO `mmpt_indent` VALUES (33, 8, 1515557404, '1', '0', 19, 1, 3);

-- ----------------------------
-- Table structure for mmpt_picture
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_picture`;
CREATE TABLE `mmpt_picture`  (
  `t_id` int NOT NULL AUTO_INCREMENT COMMENT '图片id',
  `images` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '商品图片',
  `g_id` int NULL DEFAULT 0 COMMENT '商品id',
  PRIMARY KEY (`t_id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 45 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_picture
-- ----------------------------
INSERT INTO `mmpt_picture` VALUES (12, '/image/20180109/cbc426a4e9ac5b290ae0687a5ddf626e.png', 79);
INSERT INTO `mmpt_picture` VALUES (13, '/image/20180109/e4bba1b59c31d1f58a0c2bbfac8d22c9.jpg', 80);
INSERT INTO `mmpt_picture` VALUES (14, '/image/20180109/a40a5bd2ef0b3cd585974ca98e1b93c3.jpg', 81);
INSERT INTO `mmpt_picture` VALUES (15, '/image/20180109/26d4a1643b087fe00d4a6b84acf73c63.jpg', 82);
INSERT INTO `mmpt_picture` VALUES (16, '/image/20180109/b303006fad683a2f44b29ece84517f1f.jpg', 83);
INSERT INTO `mmpt_picture` VALUES (17, '/image/20180109/b84da295d2836354f24d8c7900d9bd36.jpg', 84);
INSERT INTO `mmpt_picture` VALUES (18, '/image/20180109/f1268058e0183795a71d1ac507f1d2a5.jpg', 85);
INSERT INTO `mmpt_picture` VALUES (19, '/image/20180109/daeb96c67ef0cee91e40b9d0f4af83dd.jpg', 86);
INSERT INTO `mmpt_picture` VALUES (20, '/image/20180109/efceb903a96306920089637e7f06813a.jpg', 87);
INSERT INTO `mmpt_picture` VALUES (21, '/image/20180109/e86277ddc4e0b23535e21325afa9350a.jpg', 88);
INSERT INTO `mmpt_picture` VALUES (22, '/image/20180109/80dcb22cb92633c3b87f91c5a841938d.jpg', 89);
INSERT INTO `mmpt_picture` VALUES (23, '/image/20180109/45424411e22b5d0d80160810ff3bd817.jpg', 90);
INSERT INTO `mmpt_picture` VALUES (24, '/image/20180109/f433e6192630d3cf16aface725e79ce0.jpg', 91);
INSERT INTO `mmpt_picture` VALUES (25, '/image/20180109/ade15d9b46cdc81743e6f10d7d21125a.jpg', 92);
INSERT INTO `mmpt_picture` VALUES (26, '/image/20180109/d204bce31819687c306bb116121f9c26.jpg', 93);
INSERT INTO `mmpt_picture` VALUES (27, '/image/20180109/a35efba680a3f9be68870301a577dff9.jpg', 94);
INSERT INTO `mmpt_picture` VALUES (28, '/image/20180109/be2a810a186651d6b547127f39d36752.png', 95);
INSERT INTO `mmpt_picture` VALUES (29, '/image/20180109/cff03d09cae95a53588c4c5566ed62e1.jpg', 96);
INSERT INTO `mmpt_picture` VALUES (30, '/image/20180109/8348b60b9dcdebd48407fe2368c9ceab.jpg', 97);
INSERT INTO `mmpt_picture` VALUES (31, '/image/20180109/96f3de1ee6e7734e9702736592d7eea6.jpg', 98);
INSERT INTO `mmpt_picture` VALUES (32, '/image/20180109/0efc439f6d0e08d080d012dd78eb4c29.jpg', 99);
INSERT INTO `mmpt_picture` VALUES (33, '/image/20180109/437b9d12c37448cc6c5dce914648ba1f.jpg', 100);
INSERT INTO `mmpt_picture` VALUES (34, '/image/20180109/3ead6700210a1bcc3b525892b3475ff4.jpg', 101);
INSERT INTO `mmpt_picture` VALUES (36, '/image/20180109/5b4546cbd4a7ed3faeef1fb4b6f425a7.jpg', 102);
INSERT INTO `mmpt_picture` VALUES (37, '/image/20180109/fe7d09cae2ee9d84ba54dc1f14ec5616.jpg', 105);
INSERT INTO `mmpt_picture` VALUES (38, '/image/20180109/af55b97e20bc0b16620183806c07c01d.jpg', 103);
INSERT INTO `mmpt_picture` VALUES (39, '/image/20180110/40c843a18133f9cdd78d0fe376b457a9.jpg', 106);
INSERT INTO `mmpt_picture` VALUES (40, '/image/20180110/2db0323437247365499e91c48b4b9c2b.jpg', 107);
INSERT INTO `mmpt_picture` VALUES (41, '/image/20180110/a1f505df12c2405086395325e8dd8363.jpg', 109);
INSERT INTO `mmpt_picture` VALUES (42, '/image/20180110/1f987580031e5a460ecf612a0a25e9ff.jpg', 110);
INSERT INTO `mmpt_picture` VALUES (44, '/image/20180110/faf3bac2a163f94aa991123f4ef41a2f.jpg', 111);

-- ----------------------------
-- Table structure for mmpt_receiving
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_receiving`;
CREATE TABLE `mmpt_receiving`  (
  `rid` int NOT NULL AUTO_INCREMENT COMMENT '收货地址序号',
  `rnom` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '收件人',
  `raddress` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '真实地址',
  `rphone` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '电话',
  `remail` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '邮箱',
  `ralias` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '收货别称',
  `rdefault` int NOT NULL DEFAULT 0 COMMENT '是否默认是否地址 0-否 1-是',
  `uid` int NOT NULL DEFAULT 0 COMMENT '用户id',
  PRIMARY KEY (`rid`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 9 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_receiving
-- ----------------------------
INSERT INTO `mmpt_receiving` VALUES (6, 'Jenick', '广东省深圳市福田区****', '18898362532', '912966046@qq.com', 'Jenick', 1, 18);
INSERT INTO `mmpt_receiving` VALUES (8, '王锦佳', '5动710', '13076502809', '1269886839@qq.com', '王锦佳', 1, 19);

-- ----------------------------
-- Table structure for mmpt_shop
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_shop`;
CREATE TABLE `mmpt_shop`  (
  `s_id` int NOT NULL AUTO_INCREMENT COMMENT '购物车id',
  `time` int NULL DEFAULT 0 COMMENT '加入购物车时间',
  `g_id` int NULL DEFAULT 0 COMMENT '商品id',
  `s_num` int NULL DEFAULT 1 COMMENT '商品数量',
  `uid` int NOT NULL DEFAULT 0,
  PRIMARY KEY (`s_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_shop
-- ----------------------------

-- ----------------------------
-- Table structure for mmpt_user
-- ----------------------------
DROP TABLE IF EXISTS `mmpt_user`;
CREATE TABLE `mmpt_user`  (
  `uid` int NOT NULL AUTO_INCREMENT COMMENT '用户id',
  `uname` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '用户名',
  `password` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '用户登录密码',
  `usalt` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NOT NULL DEFAULT '' COMMENT '秘钥',
  `unom` varchar(30) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '真实姓名',
  `telephone` varchar(11) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '用户电话',
  `uemail` varchar(255) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '' COMMENT '用户邮箱',
  `create_time` int NULL DEFAULT 0 COMMENT '加入时间',
  `status` int NOT NULL DEFAULT 1 COMMENT '用户状态 0-禁用 1-启用',
  `paypass` varchar(32) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT '',
  PRIMARY KEY (`uid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 20 CHARACTER SET = utf8mb3 COLLATE = utf8mb3_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of mmpt_user
-- ----------------------------
INSERT INTO `mmpt_user` VALUES (18, 'Jenick', 'bb2daa60c1bf37d78071bef2aa0b881e', 'mmpt', 'Jenick', '18898362532', '912966046@qq.com', 1515496687, 1, 'a40eb28c3ff19497033e5669daf779ae');
INSERT INTO `mmpt_user` VALUES (19, 'wangjinjia', 'fd06439796bc6daca71ba2b8cc728ef6', 'mmpt', '', '', '', 1515554719, 1, 'cbb472ff583fead06905b68ffb2f1adb');

-- ----------------------------
-- Table structure for tp5_tb_goods
-- ----------------------------
DROP TABLE IF EXISTS `tp5_tb_goods`;
CREATE TABLE `tp5_tb_goods`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `product_id` varchar(20) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `product_name` varchar(100) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  `price` decimal(10, 0) NULL DEFAULT NULL,
  `describes` text CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL,
  `suppliers` varchar(50) CHARACTER SET utf8mb3 COLLATE utf8mb3_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 13 CHARACTER SET = latin1 COLLATE = latin1_swedish_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of tp5_tb_goods
-- ----------------------------
INSERT INTO `tp5_tb_goods` VALUES (1, '2023041012', '消毒柜修改', 4393222, '三层消毒柜\r\n修改修改修改修改修改修改修改', '广州万宝修改');
INSERT INTO `tp5_tb_goods` VALUES (2, '202304100', '小型消毒碗柜', 288, '志高（CHIGO）消毒柜家用柜式餐具厨房碗筷立式高温臭氧小型消毒碗柜商用台式大型二星级消毒柜 RTP50 适用1-3人，效果良好', '广东志高');
INSERT INTO `tp5_tb_goods` VALUES (4, '202304201', '荣耀Magic5', 4288, '荣耀Magic5屏内指纹超感光徕卡三摄手机 亮黑色 全网通（12G+256G）', '荣耀');
INSERT INTO `tp5_tb_goods` VALUES (5, '202304202', '华为（HUAWEI）nova8', 3299, '华为（HUAWEI）nova8 手机 苏音蓝 9800万全网通(8+128GB）', '华为');
INSERT INTO `tp5_tb_goods` VALUES (6, '202304203', 'Reno 全面屏拍照手机', 3599, 'OPPO Reno 全面屏拍照手机 8G+256G 雾海绿 全网通 移动联通电信 双卡双待手机', 'OPPO');
INSERT INTO `tp5_tb_goods` VALUES (11, '202304222', ' Redmi K50Pro', 2619, 'Redmi K50Pro 天玑9000 AMOLED 2K柔性直屏 OIS光学防抖 120W快充 墨羽 8GB+256GB 5G智能手机 小米红米 ', '小米');
INSERT INTO `tp5_tb_goods` VALUES (12, '21222222222', '21222222222222', 2122, '212222', '212');

SET FOREIGN_KEY_CHECKS = 1;
