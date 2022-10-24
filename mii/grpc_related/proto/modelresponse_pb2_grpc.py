# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mii.grpc_related.proto.modelresponse_pb2 as modelresponse__pb2


class ModelResponseStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GeneratorReply = channel.unary_unary(
                '/modelresponse.ModelResponse/GeneratorReply',
                request_serializer=modelresponse__pb2.MultiStringRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.MultiStringReply.FromString,
                )
        self.ClassificationReply = channel.unary_unary(
                '/modelresponse.ModelResponse/ClassificationReply',
                request_serializer=modelresponse__pb2.SingleStringRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
                )
        self.QuestionAndAnswerReply = channel.unary_unary(
                '/modelresponse.ModelResponse/QuestionAndAnswerReply',
                request_serializer=modelresponse__pb2.QARequest.SerializeToString,
                response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
                )
        self.FillMaskReply = channel.unary_unary(
                '/modelresponse.ModelResponse/FillMaskReply',
                request_serializer=modelresponse__pb2.SingleStringRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
                )
        self.TokenClassificationReply = channel.unary_unary(
                '/modelresponse.ModelResponse/TokenClassificationReply',
                request_serializer=modelresponse__pb2.SingleStringRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.SingleStringReply.FromString,
                )
        self.ConversationalReply = channel.unary_unary(
                '/modelresponse.ModelResponse/ConversationalReply',
                request_serializer=modelresponse__pb2.ConversationRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.ConversationReply.FromString,
                )
        self.Txt2ImgReply = channel.unary_unary(
                '/modelresponse.ModelResponse/Txt2ImgReply',
                request_serializer=modelresponse__pb2.MultiStringRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.ImageReply.FromString,
                )
        self.Txt2MeshReply = channel.unary_unary(
                '/modelresponse.ModelResponse/Txt2MeshReply',
                request_serializer=modelresponse__pb2.MultiStringRequest.SerializeToString,
                response_deserializer=modelresponse__pb2.ImageReply.FromString,
                )


class ModelResponseServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GeneratorReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ClassificationReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def QuestionAndAnswerReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FillMaskReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TokenClassificationReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ConversationalReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Txt2ImgReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Txt2MeshReply(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ModelResponseServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GeneratorReply': grpc.unary_unary_rpc_method_handler(
                    servicer.GeneratorReply,
                    request_deserializer=modelresponse__pb2.MultiStringRequest.FromString,
                    response_serializer=modelresponse__pb2.MultiStringReply.SerializeToString,
            ),
            'ClassificationReply': grpc.unary_unary_rpc_method_handler(
                    servicer.ClassificationReply,
                    request_deserializer=modelresponse__pb2.SingleStringRequest.FromString,
                    response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
            ),
            'QuestionAndAnswerReply': grpc.unary_unary_rpc_method_handler(
                    servicer.QuestionAndAnswerReply,
                    request_deserializer=modelresponse__pb2.QARequest.FromString,
                    response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
            ),
            'FillMaskReply': grpc.unary_unary_rpc_method_handler(
                    servicer.FillMaskReply,
                    request_deserializer=modelresponse__pb2.SingleStringRequest.FromString,
                    response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
            ),
            'TokenClassificationReply': grpc.unary_unary_rpc_method_handler(
                    servicer.TokenClassificationReply,
                    request_deserializer=modelresponse__pb2.SingleStringRequest.FromString,
                    response_serializer=modelresponse__pb2.SingleStringReply.SerializeToString,
            ),
            'ConversationalReply': grpc.unary_unary_rpc_method_handler(
                    servicer.ConversationalReply,
                    request_deserializer=modelresponse__pb2.ConversationRequest.FromString,
                    response_serializer=modelresponse__pb2.ConversationReply.SerializeToString,
            ),
            'Txt2ImgReply': grpc.unary_unary_rpc_method_handler(
                    servicer.Txt2ImgReply,
                    request_deserializer=modelresponse__pb2.MultiStringRequest.FromString,
                    response_serializer=modelresponse__pb2.ImageReply.SerializeToString,
            ),
            'Txt2MeshReply': grpc.unary_unary_rpc_method_handler(
                    servicer.Txt2MeshReply,
                    request_deserializer=modelresponse__pb2.MultiStringRequest.FromString,
                    response_serializer=modelresponse__pb2.ImageReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'modelresponse.ModelResponse', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ModelResponse(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GeneratorReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/GeneratorReply',
            modelresponse__pb2.MultiStringRequest.SerializeToString,
            modelresponse__pb2.MultiStringReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ClassificationReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/ClassificationReply',
            modelresponse__pb2.SingleStringRequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def QuestionAndAnswerReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/QuestionAndAnswerReply',
            modelresponse__pb2.QARequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FillMaskReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/FillMaskReply',
            modelresponse__pb2.SingleStringRequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TokenClassificationReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/TokenClassificationReply',
            modelresponse__pb2.SingleStringRequest.SerializeToString,
            modelresponse__pb2.SingleStringReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ConversationalReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/ConversationalReply',
            modelresponse__pb2.ConversationRequest.SerializeToString,
            modelresponse__pb2.ConversationReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Txt2ImgReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/Txt2ImgReply',
            modelresponse__pb2.MultiStringRequest.SerializeToString,
            modelresponse__pb2.ImageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Txt2MeshReply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/modelresponse.ModelResponse/Txt2MeshReply',
            modelresponse__pb2.MultiStringRequest.SerializeToString,
            modelresponse__pb2.ImageReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
