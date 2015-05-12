def collide(self, speed, blocks):

    for block in [blocks[i] for i in self.rect.collidelistall(blocks)]:

        if speed[0] > 0: self.rect.right = block.rect.left
        if speed[0] < 0: self.rect.left = block.rect.right

        if speed[1] > 0: self.rect.bottom = block.rect.top

        if speed[1] < 0: self.rect.top = block.rect.bottom