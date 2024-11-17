<template>
	<view>
		<view class="topic-top">
			<view class="topic-title">
				<navigator url="/pages/user/user" open-type="switchTab">
					<view>
						追踪
					</view>
				</navigator>
				<navigator url="/pages/user/user" open-type="switchTab">
					<view style="font-weight: 600;">
						话题榜
					</view>
				</navigator>
				<navigator url="/pages/user/user" open-type="switchTab">
					<view>
						观点榜
					</view>
				</navigator>
			</view>
			<view class="toopic-img">
				<image src="../../static/news/sousuo2.png" style="width: 35rpx;" mode="widthFix"></image>
			</view>
		</view>

		<view class="news">
			<view class="box">
				<view class="">
					<image style="width: 35rpx;" src="../../static/news/t1.png" mode="widthFix"></image>
				</view>
				<view class="news-box">
					<view class="title">
						<text>曼联客场不败场次在英超排名第二,阿森纳27次客场不败</text>
					</view>
					<view class="text">
						<text>曼联客场对阵阿斯顿维拉，这场比赛的结果对于现阶段的曼联来说影响并不是很大，但如果一旦曼联输球，他们的同城死敌曼城就将提前加冕本赛季的英超冠军。在这样的大背景下，曼联众将士自然是不愿意间接助攻死敌夺冠，因此在上半场落后的情况下，曼联在下半场发起了猛烈地反扑，最终红魔以3-1的比分战胜了对手。</text>
					</view>
					<view class="pl">
						<view class="pl-img">
							<image class="img1" src="../../static/news/y10.jpg" mode="widthFix"></image>
							<image class="img2" src="../../static/news/y3.jpg" mode="widthFix">
							<image class="img3" src="../../static/news/y6.jpg" mode="widthFix">
							<image class="img4" src="../../static/news/y5.jpg" mode="widthFix">
						</view>
						<view class="pl-num">
							<text>119 观点</text>
						</view>
					</view>
				</view>
			</view>
			<view class="box">
				<view class="">
					<image style="width: 35rpx;" src="../../static/news/t2.png" mode="widthFix"></image>
				</view>
				<view class="news-box">
					<view class="title">
						<text>司机为救婴儿闯红灯</text>
					</view>
					<view class="text">
						<text>网红约司机为救婴儿连闯3红灯，警察查实后取消处罚。</text>
					</view>
					<view class="pl">
						<view class="pl-img">
							<image class="img1" src="../../static/news/y4.jpg" mode="widthFix">
							<image class="img2" src="../../static/news/y2.jpg" mode="widthFix">
							<image class="img3" src="../../static/news/y8.jpg" mode="widthFix">
							<image class="img4" src="../../static/news/y8.jpg" mode="widthFix">
						</view>
						<view class="pl-num">
							<text>119 观点</text>
							<text class="re">热</text>
						</view>
					</view>
				</view>
			</view>

		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {

		}
	}
</script>

<style lang="scss">
	.topic-top {
		position: fixed;
		left: 0;
		right: 0;
		z-index: 1;
		background-color: #eee;
		width: 100%;
		display: flex;
		justify-content: space-between;
		padding: 10rpx 15rpx 15rpx 10rpx;
		box-sizing: border-box;
		height: 70rpx;

		.topic-title {
			width: 100%;
			display: flex;

			view {
				font-size: 40rpx;
				margin-right: 10px;
			}
		}

		.toopic-img {
			margin-right: 50rpx;
		}
	}

	.news {
		width: 100%;
		padding-top: 35px;

		.box {
			border-bottom: 1px solid #eee;
		}

		.news-box {
			padding: 15rpx;
			box-sizing: border-box;

			.title {
				font-size: 35rpx;
				font-weight: 600;
			}

			.text {
				font-size: 35rpx;
			}

			.pl {
				margin-top: 15rpx;
				display: flex;

				.pl-img {
					position: relative;
				}

				.pl-img image {
					width: 30rpx;
					height: 30rpx;
					position: absolute;
				}

				.pl-img .img1 {
					left: 20rpx;
				}

				.pl-img .img2 {
					left: 40rpx;
				}

				.pl-img .img3 {
					left: 60rpx;
				}

				.pl-img .img4 {
					left: 80rpx;
				}

				.pl-num {
					margin-left: 60px;
					font-size: 20rpx;
					.re{
						margin-left: 20rpx;
						padding: 0 15rpx;
						color: red;
						border: 1px solid red;
						border-radius: 10rpx;
					}
				}
			}
		}
	}
</style>
