<template>
	<view>
		<view class="header">
			<scroll-view scroll-x="true" style="white-space: nowrap;" scroll-with-animation="true">
				<view class="tabs">
					<view class="imgBox">
						<image src="../../static/news/shouhu.png" mode="widthFix"></image>
					</view>
					<view v-for="(item,index) in tabs" :key="index">
						{{ item }}
					</view>
				</view>
			</scroll-view>
			<view class="weather">
				<text>4°C 小雨 桂林 PM2.59</text>
				<view class="search">搜索关键字</view>
			</view>
		</view>
		<view class="hot">
			<view v-for="(item,index) in hot" :key="index">
				<view class="title">{{ item.title }}</view>
				<view class="msg">
					<text class="red">置顶</text>
					<text>{{item.author}} </text>
					<text>{{item.comment_num}}评</text>
				</view>
			</view>
		</view>
		<view class="news">
			<view v-for="(item,index) in news" :key="index">
				<view class="top">
					<view class="img">
						<image :src="item.picture" mode="widthFix"></image>
					</view>
					<view class="title">
						{{ item.title }}
					</view>
				</view>
				<view class="bottom">
					<text>{{item.author}}</text>
					<text class="comment">{{item.comment_num}}评</text>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				tabs: ['要闻', '推荐', '关注流', '24小时', '娱乐', '桂林', '财经', '生活', '科技', '军事', '体育', '汽修', '健康', '国际', '千里眼', '5G'],
				hot: [{
					title: "2020,我们温暖的记忆",
					author: "新闻联播",
					comment_num: 45
				}, {
					title: "森林大县57年无大火是怎么样做到",
					author: "光明网",
					comment_num: 17
				}],
				news: [{
						picture: "../../static/news/xw10.png",
						title: "中国老年化水平加速,论养老保险在中国的重要性?人们应不应该买保险?",
						author: "心京报官微",
						comment_num: 58
					},
					{
						picture: "../../static/news/b.png",
						title: "人们都喜欢聚在一起玩耍,人们聚集在一起欢呼是好?是坏?",
						author: "烽火君",
						comment_num: 18
					},
					{
						picture: "../../static/news/d.png",
						title: '几年近疯狂,涉案金额超3亿,一个"背包客"牵出全国跨省"倒烟"大案',
						author: "大河网",
						comment_num: 38
					},
					{
						picture: "../../static/news/d.png",
						title: '几年近疯狂,涉案金额超3亿,一个"背包客"牵出全国跨省"倒烟"大案',
						author: "大河网",
						comment_num: 38
					},
					{
						picture: "../../static/news/d.png",
						title: '几年近疯狂,涉案金额超3亿,一个"背包客"牵出全国跨省"倒烟"大案',
						author: "大河网",
						comment_num: 38
					},
					{
						picture: "../../static/news/d.png",
						title: '几年近疯狂,涉案金额超3亿,一个"背包客"牵出全国跨省"倒烟"大案',
						author: "大河网",
						comment_num: 38
					}
				]
			}
		},
		methods: {

		}
	}
</script>

<style lang="scss">
	.header {
		background-color: #dd524d;
		color: #fff;

		.tabs {
			display: inline-block;
			display: flex;
			align-items: center;

			.imgBox image {
				width: 40rpx;
			}

			view {
				padding: 10px 5px;
			}
		}
	}

	.weather {
		display: flex;
		justify-content: space-between;
		padding: 5px;

		.search {
			font-size: 22rpx;
			text-align: center;
			padding: 3px 20px;
			background-color: #fff;
			color: #555;
			border-radius: 25px;
		}
	}
	
	.hot{
		padding: 5px;
		border-bottom: 1px solid #c1c1c1;
		> view{
			padding: 5px;
			.msg{
				font-size: 22rpx;
				text{
					display: inline-block;
					margin: 0 10px;
					padding-top:2px;
				}
				.red{
					color: #dd524d;
				}
			}
		}

		
	}
	
	.news{
		padding: 5px 0;
		>view{
			padding: 10px 10px;
			border-bottom: 1px solid #c1c1c1;
			.top{
				display: flex;
				image{width: 266rpx;}
				.title{font-size: 30rpx;padding-left: 20px;}
			}
			.bottom{
				text{
					display: inline-block;
					font-size: 22rpx;
					color: #b4b4b4;
				}
				.comment{
					margin-left: 10px;
				}
			}
		}
	}
</style>