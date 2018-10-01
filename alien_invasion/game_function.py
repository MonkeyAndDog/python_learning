import sys

import pygame

from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
	# 监听键盘和鼠标事件
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, ai_settings, screen, ship, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
	"""响应按键"""
	if event.key == pygame.K_RIGHT:
		# 飞船向右移动
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		# 飞船向左移动
		ship.moving_left = True
	elif event.key == 0: # 这可能是个虚拟机或者python的bug，K_SPACE的值为32， 空格为0
		# 子弹发射
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_events(event, ship):
	if event.key == pygame.K_RIGHT:
		# 停止飞船向右移动
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		# 停止飞船向左移动
		ship.moving_left = False

def update_screen(ai_settings, screen, ship, bullets):
	"""更新屏幕函数"""
	# 设置背景颜色
	screen.fill(ai_settings.bg_color)

	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	# 绘制飞船
	ship.blitme()
	
	# 让最近绘制的屏幕可见
	pygame.display.flip()
