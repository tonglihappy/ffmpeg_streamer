CROSS =
CC = $(CROSS)gcc

CFLAGS = -O3 -DNDEBUG -Wall -c

SRCS = $(wildcard ./src/*.c)
OBJS = $(patsubst %.c, %.o, $(SRCS))

HEADER_PATH = -I./include/
LIB_PATH = -L./lib/

LIBS = -lavformat -lavcodec -lswscale -lavutil -lavfilter -lswresample -lavdevice -lpostproc -lx264 -ldl -lz -lm -lrt -lpthread

VERSION = 1.0.0.1

TARGET = ffmpeg

$(TARGET) : $(OBJS)
	$(CC) $^ -o $@ $(LIB_PATH) $(LIBS)

$(OBJS):%.o : %.c
	$(CC) $(CFLAGS) $< -o $@ $(HEADER_PATH)

clean:
	rm -rf $(TARGET) ./src/*.o
