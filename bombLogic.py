if keys[pygame.K_SPACE] and bomb1quantity == 0 and player1.alive:
                if player1.rect.x % 32 < 16 and player1.rect.y % 32 < 16:
                    if player1.megabombs:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32 + 3),
                                           (
                            player1.rect.y - player1.rect.y % 32 + 1), 32, 32, 0,1))
                        player1.megabombcount-=1
                    else:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32+3),
                                        (
                            player1.rect.y - player1.rect.y % 32+1), 32, 32, 0,0))
                elif player1.rect.x % 32 < 16 and player1.rect.y % 32 >= 16:
                    if player1.megabombs:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32 + 3),
                                           (
                            player1.rect.y - player1.rect.y % 32 + 33), 32, 32, 0, 1))
                        player1.megabombcount -= 1
                    else:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32+3),
                                        (
                            player1.rect.y - player1.rect.y % 32+33), 32, 32, 0,0))
                elif player1.rect.x % 32 >= 16 and player1.rect.y % 32 < 16:
                    if player1.megabombs:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32 + 35),
                                           (
                            player1.rect.y - player1.rect.y % 32 + 1), 32, 32, 0, 1))
                        player1.megabombcount -= 1
                    else:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32+35),
                                        (
                            player1.rect.y - player1.rect.y % 32+1), 32, 32, 0,0))
                else:
                    if player1.megabombs:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32 + 35),
                                           (
                            player1.rect.y - player1.rect.y % 32 + 33), 32, 32, 0, 1))
                        player1.megabombcount -= 1
                    else:
                        bombs1.append(bomb((
                            player1.rect.x - player1.rect.x % 32+35),
                                        (
                            player1.rect.y - player1.rect.y % 32+33), 32, 32, 0,0))
                bomb1quantity = 1
            if keys[pygame.K_SLASH] and bomb2quantity == 0 and player2.alive:
                if player2.rect.x % 32 < 16 and player2.rect.y % 32 < 16:
                    if player2.megabombs:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32 + 3),
                                           (
                            player2.rect.y - player2.rect.y % 32 + 1), 32, 32, 0,1))
                        player2.megabombcount -= 1
                    else:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32+3),
                                        (
                            player2.rect.y - player2.rect.y % 32+1), 32, 32, 0,0))
                elif player2.rect.x % 32 < 16 and player2.rect.y % 32 >= 16:
                    if player2.megabombs:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32 + 3),
                                           (
                            player2.rect.y - player2.rect.y % 32 + 33), 32, 32, 0, 1))
                        player2.megabombcount -= 1
                    else:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32+3),
                                    (
                            player2.rect.y - player2.rect.y % 32+33), 32, 32, 0,0))

                elif player2.rect.x % 32 >= 16 and player2.rect.y % 32 < 16:
                    if player2.megabombs:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32 + 35),
                                           (
                            player2.rect.y - player2.rect.y % 32 + 1), 32, 32, 0, 1))
                        player2.megabombcount -= 1
                    else:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32+35),
                                    (
                            player2.rect.y - player2.rect.y % 32+1), 32, 32, 0,0))

                else:
                    if player2.megabombs:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32 + 35),
                                           (
                            player2.rect.y - player2.rect.y % 32 + 33), 32, 32, 0, 1))
                        player2.megabombcount -= 1
                    else:
                        bombs2.append(bomb((
                            player2.rect.x - player2.rect.x % 32+35),
                                    (
                            player2.rect.y - player2.rect.y % 32+33), 32, 32, 0,0))